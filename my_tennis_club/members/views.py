from django.http import HttpResponse
from django.template import loader
from .form import EmpForm
from .form import PostForm
from django.shortcuts import render
import random
from .models import Student
from .models import BlogPost


def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


def test(request):
  templateName = loader.get_template('name.html')

  context = \
  {
    "firstName": "Rick",
    "lastName": "Divietro"
  }

  return HttpResponse(templateName.render(context, request))


def index(request):
  templateIndex = loader.get_template("index.html")

  return HttpResponse(templateIndex.render())


def module(request):
  templateModule = loader.get_template('module.html')

  stu = EmpForm()

  return render(request, "module.html", {'form': stu})


def template_view(request):
  stu = EmpForm()

  myForm = EmpForm(request.POST)

  if myForm.is_valid():
    name = myForm.cleaned_data["first_name"]
    surname = myForm.cleaned_data["last_name"]
    num = random.randint(0, 100000)

    string = Student(num, name, surname)

    string.save()

  return render(request, "module.html", {"form": stu})


def home_view(request):
  myMembers = Student.objects.all().values()
  template = loader.get_template('home.html')

  context = {
    'myMembers': myMembers,
  }
  return HttpResponse(template.render(context, request))


def blog_view(request):
  post = PostForm()

  myBlog = PostForm(request.POST)

  if myBlog.is_valid():
    title = myBlog.cleaned_data["title"]
    author = myBlog.cleaned_data["author"]
    context = myBlog.cleaned_data["context"]
    tag = myBlog.cleaned_data["tag"]

    num = random.randint(0, 100000)
    saved = BlogPost(num, title, context, author, tag)

    saved.save()

  return render(request, "blog.html", {"form": post})


def blog_db(request):
  myBlog = BlogPost.objects.all().values()
  template = loader.get_template('post.html')

  context = \
  {
    'myBlog': myBlog,
  }
  return HttpResponse(template.render(context, request))


def results_view(request):
  name = ""
  tag = ""

  myForm = (request.POST)
  dict = myForm.dict()

  if len(dict) != 0:
    name = (dict["name"])
    tag = (dict["tag"])

    if name and not tag:
      myData = BlogPost.objects.filter(author=name).values()

    elif tag and not name:
      myData = BlogPost.objects.filter(tag=tag).values()

    else:
      myData = BlogPost.objects.filter(author=name, tag=tag).values()


    context = \
    {
      'myRes': myData,
    }

  return render(request, "results.html", context)

def delete(request, id):
  selection = BlogPost.objects.get(id=id)
  selection.delete()

  return render(request, "delete.html")


def search(request):
  return render(request, "search.html")


def tag(request, tag):
  myData = BlogPost.objects.filter(tag=tag).values()

  context = \
  {
    "tag": tag,
    "myRes": myData,
  }

  return render(request, "tag.html", context)