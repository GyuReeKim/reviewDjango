from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
# decorators도 잘 알아둬야 한다.

# Create your views here.
def index(request):
    # raise : 강제로 오류 발생
    # user : login한 사용자
    # get : get방식으로 들어오는 data
    # post : post방식으로 들어오는 data
    # files : image file 등
    return render(request, 'posts/index.html')

def detail(request, id):
    post = get_object_or_404(Post, id=id)

def create(request):
    pass