from django.db import models
from django.db.models.fields import  exceptions #引入错误计划
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
# 富文本编辑模块
from ckeditor_uploader.fields import RichTextUploadingField
from  read_statistics.models import ReadNumExpandMethod,ReadDateDetail


# Create your models here.

 # 博客分类
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

# 博客的内容
class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDateDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time'] #排序
        verbose_name = '博客' # 设置模型别名
        verbose_name_plural =verbose_name #设置复数格式也是模型别名


