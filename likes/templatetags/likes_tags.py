from  django import template
from  django.contrib.contenttypes.models import ContentType
from ..models import LikeCount,LikeRecount

register = template.Library()

@register.simple_tag
def get_like_count(obj):
    like_content_type = ContentType.objects.get_for_model(obj)
    like_count, created = LikeCount.objects.get_or_create(content_type=like_content_type,object_id=obj.pk)
    return like_count.liked_num

@register.simple_tag(takes_context=True)
def get_like_status(context,obj):
    like_content_type = ContentType.objects.get_for_model(obj)
    user = context['user']
    if not user.is_authenticated:
        return ''
    if LikeRecount.objects.filter(content_type=like_content_type,object_id=obj.pk,user=user).exists():
        return 'active'
    else:
        return ''

@register.simple_tag
def get_content_type(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return content_type.model