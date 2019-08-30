from django import template
from  django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm
#  ..表示上层文件夹
# 自定义模板标签，创建后需要重启后才能注册成功
register = template.Library()

@register.simple_tag
def get_comment_count(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    comment_count = Comment.objects.filter(content_type=blog_content_type, object_id=obj.pk).count()
    return comment_count

@register.simple_tag
def get_comment_form(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    data = {}
    data['content_type'] = blog_content_type.model
    data['object_id'] = obj.pk
    data['reply_comment_id'] = 0
    comment_from = CommentForm(initial=data)
    return  comment_from

@register.simple_tag
def get_comment_list(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    comment = Comment.objects.filter(content_type=blog_content_type, object_id=obj.pk, parent=None)
    return  comment.order_by('-comment_time')