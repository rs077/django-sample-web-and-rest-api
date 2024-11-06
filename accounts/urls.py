from django.urls import path
from .views import SignUpView, account

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]