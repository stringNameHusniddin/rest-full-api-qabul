from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, surname, fatherName, viloyat, tuman, mahalla, polikilinika, uy, tel, password=None):
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			surname=surname,
			fatherName=fatherName,
			viloyat=viloyat,
			tuman=tuman,
			mahalla=mahalla,
			polikilinika=polikilinika,
			uy=uy,
			tel=tel
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, surname, fatherName, viloyat, tuman, mahalla, polikilinika, uy, tel, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			surname=surname,
			fatherName=fatherName,
			viloyat=viloyat,
			tuman=tuman,
			mahalla=mahalla,
			polikilinika=polikilinika,
			uy=uy,
			tel=tel
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email = models.EmailField(max_length=200)
	username = models.CharField(max_length=200, unique=True)
	surname = models.CharField(max_length=200)
	fatherName = models.CharField(max_length=200)
	viloyat = models.CharField(max_length=200)
	tuman = models.CharField(max_length=200)
	mahalla = models.CharField(max_length=200)
	polikilinika = models.IntegerField()
	uy = models.IntegerField()
	tel = models.CharField(max_length=9)
	born_at = models.DateField(blank=True, null=True)


	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'surname', 'fatherName', 'viloyat', 'tuman', 'mahalla', 'polikilinika', 'uy', 'tel']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
	
class Post(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	body = models.TextField()
	bulim = models.CharField(max_length=200)
	doktor = models.CharField(max_length=200)
	xona = models.IntegerField()


class Bulim(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Doktor(models.Model):
    name = models.CharField(max_length=200)
    bulim = models.ForeignKey(Bulim, on_delete=models.CASCADE)
    xona = models.IntegerField()

    def __str__(self):
        return self.name

