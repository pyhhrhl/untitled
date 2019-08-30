from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.db.models import  ObjectDoesNotExist
from .models import LikeCount,LikeRecount

def ErrorResponse(code,message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data) # 记住，重点，细节

def SuccessResponse(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return JsonResponse(data)

# Create your views here.
def like_change(request):
    #获取数据
    user = request.user

    if not user.is_authenticated:
        return ErrorResponse(400,'您未登录')

    content_type = request.GET.get('content_type')
    object_id = request.GET.get('object_id')

    try:
        content_type = ContentType.objects.get(model=content_type)
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(400, '点赞对象不存在')

    is_like = request.GET.get('is_like')

    #处理数据
    if is_like == 'true':
        #要点赞
        like_record,created = LikeRecount.objects.get_or_create(content_type=content_type,object_id=object_id,user=user)
        if created:
            # 未点赞，进行点赞
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.liked_num += 1
            like_count.save()
            return SuccessResponse(like_count.liked_num)
        else:
            #已点赞过，不能重复点赞
            return ErrorResponse(402,'您已经点赞，不能重复点赞')
    else:
        #取消点赞
        if LikeRecount.objects.filter(content_type=content_type,object_id=object_id,user=user).exists():
            # 有点赞过，取消点赞
            like_record = LikeRecount.objects.get(content_type=content_type,object_id=object_id,user=user)
            like_record.delete()
            # 总点赞数量减一
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return SuccessResponse(like_count.liked_num)
            else:
                return ErrorResponse(404,'数据错误')
        else:
            # 没有点赞过，返回错误信息
            return ErrorResponse(402,'您没有点赞，不能取消')