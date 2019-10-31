from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name="index"), # views안의 index 함수를 실행시킨다.
    path('<int:id>/', views.detail, name="detail"),
]