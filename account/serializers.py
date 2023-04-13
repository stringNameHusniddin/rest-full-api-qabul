from rest_framework import serializers
from .models import Account, Post, Doktor, Bulim

class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'surname', 'fatherName', 'viloyat', 'tuman', 'mahalla', 'polikilinika', 'uy', 'tel', 'born_at',  'password', ]
        extra_kwargs = {
			'password': {'write_only': True},
		}	

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            surname=self.validated_data['surname'],
            fatherName=self.validated_data['fatherName'],
            viloyat=self.validated_data['viloyat'],
            tuman=self.validated_data['tuman'],
            mahalla=self.validated_data['mahalla'],
            polikilinika=self.validated_data['polikilinika'],
            uy=self.validated_data['uy'],
            tel=self.validated_data['tel'],
            born_at=self.validated_data['born_at'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
    
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post

class DoktorSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Doktor

class BulimSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bulim