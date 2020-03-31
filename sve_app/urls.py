from django.urls import re_path,path
from . import views
# from django.contrib.auth import views
from django.urls import reverse_lazy


urlpatterns = [
    re_path(r'^$', views.MainView.as_view(), name='main'),

    re_path(r'^list/$', views.PostListView.as_view(), name='prime_list'),
    
    re_path(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name='new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name='edit'),
    re_path(r'^drafts/$', views.DraftPostView.as_view(), name='draft_list'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name='remove'),
    re_path(r'^post/(?P<pk>\d+)/selling/$', views.transferitm, name='selling'),
    re_path(r'^post/(?P<pk>\d+)/buying/$', views.buy, name='buying'),
    re_path(r'^post/cart/$', views.cart, name='cart'),

    re_path(r'^post/(?P<pk>\d+)/publishp/$', views.item_saled, name='item_saled')
]