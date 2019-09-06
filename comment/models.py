import threading # 多线程库
from django.db import models
from django.contrib.auth.models import User
# 对应任何类型
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)

    # parent_id = models.IntegerField(default=0)
    root = models.ForeignKey('self',related_name='root_comment',null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',related_name='parent_comment',null=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User,related_name='reply',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_time'] #排序

    def get_url(self):
        return self.content_object.get_url()

    def get_user(self):
        return self.user