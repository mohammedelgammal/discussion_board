from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:board_id>/', views.topics, name='board_topics'),
    path('boards/<int:board_id>/new/', views.new_topic, name='new_topic')
]