from django.urls import path
from spblog import views

urlpatterns = [
        path('', views.spblog_index, name='spblog_index'),
        path('<int:pk>/', views.spblog_detail, name='spblog_detail'),
        ]
