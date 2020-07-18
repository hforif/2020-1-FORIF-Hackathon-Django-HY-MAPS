from django.db import models
from maps.models import Building
from user.models import User
# Create your models here.


class Board(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, default="가제")
    recent_revised_time = models.DateTimeField(auto_now=True)
    contents = models.TextField()


#회원들이 게시판에 글을 씀
#그 글들을 지들이 바꿀 수 있음.
#게시판의 글들에 대해서는 admin과 비슷한 능력->이걸 어떻게 구현?

#1 building : 1 board : n Post

#게시판에 필요한 것: 최종 수정 시간. 수정자(or 작성자)User와 연결
#내용(건물, 추가되는 특징)

#building = Building()
#building.cafe = "3층 로비"
#building.save()

#board = Board(building = building)

#board.building = building
#board.save()

#board.building.cafe 
#board.building.save()