from django.urls import path
from forum.views import  HomeView
from forum import views

urlpatterns= [
    
    path('', HomeView.as_view(), name="forum"),
    path('rev', views.rev, name="rev"),
    path('rev/edit/<int:pk>', views.rev_update, name='rev_update'),
    path('about', views.about, name="about"),
    path('filter/<int:pk>', views.fil, name='identity'),
    path('category/', views.cate,name="cate"),
]