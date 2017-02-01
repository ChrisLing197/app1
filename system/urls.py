from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'system'
urlpatterns = [
        url(r'^accounts/new/$', views.UserCreate.as_view(), name='register'),
        url(r'^accounts/edit/$', views.register, name='user_edit'),
        url(r'^accounts/', include('django.contrib.auth.urls')),

        url(r'^dashboard/$', views.dashboard, name='dashboard'),

        url(r'^manage/accounts/$', views.UserList.as_view(), name='user_list'),
        url(r'^manage/accounts/new$', views.StaffCreate.as_view(), name='staff_register'),
        url(r'^manage/accounts/delete/(?P<pk>[0-9]+)/', views.UserDelete.as_view(), name='user_del'),
        url(r'^manage/accounts/(?P<pk>[0-9]+)/', views.UserDetail.as_view(), name='user_detail'),

        url(r'^messages/new/', views.SendMessage.as_view(), name='send_msg'),

        url(r'^item/new/',views.NewItem.as_view(),name='post_item'),
        url(r'^add/(?P<id>[0-9]+)/',views.add,name='add'),

        url(r'^$', views.index, name='home'),
        url(r'^logout/$', views.logout_view, name='logout')
    ]
