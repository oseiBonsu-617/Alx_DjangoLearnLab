from django.urls import path, include
from rest_framework import routers
from .views import RegisterView, LoginView, ProfileView, UnfollowUserView, FollowUserView

router = routers.DefaultRouter()
router.register('register', RegisterView.as_view(), name='register')
router.register('login', LoginView.as_view(), name='register')
router.register('profile', ProfileView.as_view(), name='register')

urlpatterns = [
    path(r'', include(router.urls))
]
