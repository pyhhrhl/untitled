from django.db import models
from django.db.models.fields import  exceptions #引入错误计划
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import  timezone

# Create your models here.

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# 抽象类
class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:  # 如果提示错误提示不存在，则显示0
            return 0

class  ReadDateDetail(models.Model):
    read_num = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')