from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_name = models.CharField(max_length=100, db_index=True)
    board_status = models.IntegerField(default=0)
    last_change_board = models.DateTimeField(auto_now_add=True)
    command = models.BooleanField(default=0)

    def __str__(self):
        return "board name: {} user: {}".format(self.board_name, self.user)


class List(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, db_index=True)
    list_name = models.CharField(max_length=100, db_index=True)
    list_private = models.IntegerField(default=0)
    list_status = models.IntegerField(default=0)
    list_time_create = models.DateTimeField(auto_now_add=True)


class CardsOnList(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100, db_index=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    card_time_create = models.DateTimeField(auto_now_add=True)


class CommentsInCard(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=2000)
    comment_pub_date = models.DateTimeField(auto_now_add=True)
