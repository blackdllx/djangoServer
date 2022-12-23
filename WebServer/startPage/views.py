from .mail import main
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import Forum, Topic, EmailVerify
from django.contrib.auth.models import Group



def auth(request):
    username = request.COOKIES.get("username")
    password = request.COOKIES.get("password")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        if not username: return [False]

    my_group = Group.objects.get(name='verified')
    au = authenticate(username=username, password=password)
    ver=my_group.user_set.all()
    print(my_group.user_set.all())
    if au:
        if au in ver:
            return True
        return render(request, "login.html", {"erors": "Not verified. Please verify your account wia gmail"})
    return render(request, "login.html", {"erors": "incorect data"})


def index(request):
    # c = auth(request)
    # if c == True:
    #     username = request.COOKIES.get("username")
    #     password = request.COOKIES.get("password")
    #     forums = Forum.objects.all()
    #     response = render(request, "mainIndex.html", {"forums": forums[:3]})
    #     response.set_cookie("username", username, domain=settings.SESSION_COOKIE_DOMAIN)
    #     response.set_cookie("password", password, domain=settings.SESSION_COOKIE_DOMAIN)
    #     return response
    # return c
    # if request.user.is_authenticated:
    #     forums = Forum.objects.all()
    #     return render(request, "mainIndex.html", {"forums": forums[:3]})
    # return HttpResponse("bad")
    forums = Forum.objects.all()
    return render(request, "mainIndex.html", {"forums": forums[:3]})

def forum(request, forum_id):
    c = auth(request)
    if c == True:
        forum = Forum.objects.filter(id=forum_id)
        print(forum)
        if forum:
            forum=forum[0]
            # return HttpResponse(f"forum {forum_id} {forum.title} {forum.topic_set.all()}")
            return render(request, "forum.html", {"forum": forum, "topics": forum.topic_set.all()})
        return HttpResponse(f"forum out of range")
    return c

def topic(request, forum_id, topic_id):
    c = auth(request)
    if c:
        topic = Topic.objects.filter(id=forum_id)
        print(topic)

        if topic:
            topic = topic[0]
            print(topic.comment_set.all())
            return render(request, "topics.html", {"coments": topic.comment_set.all(), "topic": topic})
        return HttpResponse(f"forum out of range")
    return c


def verify(request, token):
    username = request.COOKIES.get("username")
    password = request.COOKIES.get("password")
    tokens = EmailVerify.objects.all()
    print(tokens)
    if tokens:
        for i in tokens:
            if token == i.link:
                my_group = Group.objects.get(name='verified')
                my_group.user_set.add(authenticate(username=username, password=password))
                i.delete()
                return HttpResponse("GOOD")
    return HttpResponse("BAD")
