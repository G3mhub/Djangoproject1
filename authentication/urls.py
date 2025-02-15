from django.urls import path,include
from authentication.views import *

urlpatterns=[
    path("", SingUpView.as_view(),name="singup"),
    path("accounts/",include("django.contrib.auth.urls")),

]