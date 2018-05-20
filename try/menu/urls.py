from django.conf.urls import url
from .views import signup, confirm_signup, login, index

urlpatterns = [
    url(r'^signup([1-3]{1})/',signup, name="signup1"),
    url(r'^confirm_signup([1-3]{1})/',confirm_signup,name="confirm"),
    url(r'login/', login, name="login"),
    url(r'^index/(?P<pk>[0-9]+)/$', index, name='index'),
]