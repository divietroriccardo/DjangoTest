from django.db import models

class Student(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)

  class Meta:
    db_table = "student"

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class BlogPost(models.Model):
  title = models.CharField(max_length=50)
  context = models.TextField(max_length=255)
  author = models.CharField(max_length=50)
  tag = models.CharField(max_length=50, null=True)
  date = models.DateTimeField(null=True, auto_now_add=True)

  class Meta:
    db_table = "blog"