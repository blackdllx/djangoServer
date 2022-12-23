from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:forum_id>', views.forum, name="forum"),
    path('<int:forum_id>/<int:topic_id>', views.topic, name="topic"),
    path('verify/<str:token>', views.verify, name="verify")
]