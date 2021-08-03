from django.urls import path,include
from login import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name="helloViewset")
router.register('userprofile',views.USerProfileViewSet)

urlpatterns = [
    
    path('loginView',views.HelloApiView.as_view()),
    path('',include(router.urls))
    

]
