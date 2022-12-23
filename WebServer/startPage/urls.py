from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.LoginView.as_view(template_name="login.html", next_page="/"), name="login"),
    path("logout/", views.LogoutView.as_view(next_page="/"), name="logout"),
    path('<int:forum_id>', views.forum, name="forum"),
    path('<int:forum_id>/<int:topic_id>', views.topic, name="topic"),
    path('verify/<str:token>', views.verify, name="verify")
]