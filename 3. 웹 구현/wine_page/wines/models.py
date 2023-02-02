from django.db import models
from tkinter.tix import DECREASING
import os
# User (장고기본모델)을 사용하기 위해 불러옴 author 필드 구현
from django.contrib.auth.models import User


class Pose(models.Model):
    name = models.CharField(max_length=30, null=False)
    enname = models.CharField(max_length=30, null=False)
