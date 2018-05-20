from django.conf.urls import url
from .views import main, submit, first

urlpatterns = [
    url(r'main/', main, name="main"),
    url(r'submit/',submit, name="submit"),
    url(r'^$',first, name="first")
]