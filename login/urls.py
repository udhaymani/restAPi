from django.urls import path,include
from login import views
urlpatterns = [
    
    path('loginView',views.HelloApiView.as_view())
]
