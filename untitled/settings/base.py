"""
Django settings for untitled project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

#;DJANGO_SETTINGS_MODULE=untitled.setting.base
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Application definition

INSTALLED_APPS = [
    # DJANGO自带的
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  #阅读计数的框架自带模板
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #第3方库
    'ckeditor',
    'ckeditor_uploader',
    # 项目APP
    'blog',
    'read_statistics',
    'comment',
    'likes',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'untitled.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 设置公共的模板变量
                'user.context_processors.login_modal_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'untitled.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 配置media (保存上传的文件)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'

CKEDITOR_CONFIGS = {
    'default': {},
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto', # 宽度
        'height': '180', #评论框高度
        'tabSpaces': 4, #table 转成4个空格
        'removePlugins': 'elementspath', # 去掉最后两行
        'resize_enabled': False, # 去掉最后两行
    }
}
# 自定义全局参数
EACH_PAGE_BLOG_NUMBER = 7

# 缓存设置
# 设置缓存后，需要执行python manage.py createcachetable
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}