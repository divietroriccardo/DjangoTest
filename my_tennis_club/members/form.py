from django import forms
from .models import Student
from .models import BlogPost

class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"