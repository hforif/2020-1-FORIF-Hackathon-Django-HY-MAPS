from django.urls import path
from . import views

app_name="postpostpost"

urlpatterns = [
    path("writinglist/<int:number>/", views.writinglist, name="writinglist"),
    path("writtencontent/<int:pk>/", views.writtencontent, name="writtencontent"),
    
    path("writingpost/<int:number>/", views.writingpost, name="writingpost"),

    path("updatingpost/<int:pk>/", views.updatingpost, name="updatingpost"),



    # path("building/<int:number>/board/" List), #여기서 포스트는 새 게시글 생성, 리스트 전체가 보임
    # path("building/<int:number>/board/<int:pk>" Detail), #여기서 포스트는 게시글 수정. 삭제, 읽기도 가능
    
]