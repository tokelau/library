from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', 'blog.views.index'),
    url(r'^blog/math/$', 'blog.views.math'),
    url(r'^blog/physics/$', 'blog.views.physics'),
    url(r'^blog/natural/$', 'blog.views.natural'),
    url(r'^blog/other/$', 'blog.views.other'),
    url(r'^blog/contacts/$', 'blog.views.contacts'),

]



