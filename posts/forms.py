from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # form을 어떤 model과 연결해줄지 설정해준다.
    class Meta:
        model = Post
        fields = '__all__'