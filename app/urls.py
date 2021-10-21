from django.urls import path

from . import views


urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('save_post/<slug:slug>/', views.save_post, name='save_post'),
	path('saved/', views.saved_posts, name='saved'),
]

