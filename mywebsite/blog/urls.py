from django.urls import path
from blog import views

# 처리 규칙 정의
urlpatterns = [
    path("", views.index, name="index"), # 아무 것도 안했을 때 메인페이지 index라는 view 처리 규칙을 따르도록
]