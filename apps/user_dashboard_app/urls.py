from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_page, name = 'login'),
    url(r'^dashboard$', views.user_dashboard, name = 'user_dashboard'),
    url(r'^user/(?P<id>\d+$)', views.user_reviews, name = 'user_reviews'),
    url(r'^register_user$', views.register_user, name='register_user'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^edit_user/(?P<id>\d+$)', views.edit_user, name='edit_user'),
    url(r'^update_user', views.update_user, name='update_user'),
    url(r'^delete_all_users$', views.purge_users),
    url(r'^logout$', views.logout, name='logout'),
]
