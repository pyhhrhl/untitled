
from django.shortcuts import get_object_or_404,render
#引入分页器
from  django.core.paginator import Paginator
from  django.conf import  settings
from  django.db.models import Count
# 本APP下所有模型
from .models import *
from  read_statistics.utils import read_statistics_once_read
# Create your views here.

# 设置分页博客数量
each_blog_num = settings.EACH_PAGE_BLOG_NUMBER

#设置分页器
def blog_paginator(request,blogs_all_list):
    page_num = request.GET.get('page', 1)  # 获取页码参数(get请求)
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, each_blog_num)  # 分页器进行分页
    total_page = paginator.num_pages
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_range = list(range(max(1, current_page_num - 2), min(current_page_num + 2, total_page) + 1))
    if page_range[0] != 1:
        if page_range[0] != 2:
            page_range.insert(0, '...')
        page_range.insert(0, 1)
    if page_range[-1] != total_page:
        if page_range[-1] != total_page - 1:
            page_range.append('...')
        page_range.append(total_page)

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_dict
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = blog_paginator(request,blogs_all_list)
    return  render(request,'blog/blog_list.html', context)

def blog_with_type(request,blog_type_pk):
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = blog_paginator(request,blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blog_with_type.html', context)

def blog_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = blog_paginator(request,blogs_all_list)
    context['blog_with_date'] = '%s年%s月' %(year,month)
    return render(request, 'blog/blogs_with_date.html', context)

def blog_detail(request, blog_pk ):

    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key =  read_statistics_once_read(request,blog)
    # 页面返回
    context = {}
    context['previous_page'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_page'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    # cookie
    response = render(request,'blog/blog_detail.html', context) #使用render
    response.set_cookie(read_cookie_key,'true')
    return  response
