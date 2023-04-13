from rest_framework import routers
from .views import AccountView, PostView, BulimView, DoktorView

route = routers.DefaultRouter()
route.register('api/user', AccountView)
route.register('api/post', PostView)
route.register('api/doktor', DoktorView)
route.register('api/bulim', BulimView)

urlpatterns=route.urls