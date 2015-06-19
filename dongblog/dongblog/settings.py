# -*- coding: utf-8 -*-
# Django settings for dongblog project.

import os
import re
from django.utils.translation import ugettext_lazy as _
from utils import FreeConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '40nlvc+^=ee1_)&x9%lv184t=#m*9sya!2k4xnoy#=6k@dx+20'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True


LANGUAGE_CODE = None
LANGUAGES = (
    ('zh-cn', u'简体中文'),
    ('en-us', 'English'),
)



LOG_ROOT = None
SITE_DOMAIN = None
MONGODB_CONF = None
UPLOAD_FILE_ROOT = '/var/app/enabled/blog-webfront/static/'

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_SUBJECT_PREFIX = '[dongblog] '

EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
SERVER_EMAIL = None

DUOSHUO_SECRET = None    # 多说分配的token
DUOSHUO_SHORT_NAME = None    # 多说上注册的二级域名



def _load_config(section, config_files):
    global DEBUG, LOG_ROOT, MONGODB_CONF, LANGUAGE_CODE, UPLOAD_FILE_ROOT, \
            SITE_DOMAIN, DATABASES, DUOSHUO_SECRET, DUOSHUO_SHORT_NAME, EMAIL_HOST_USER, \
            EMAIL_HOST_PASSWORD, SERVER_EMAIL

    cp = FreeConfigParser()
    cp.read(config_files)

    DEBUG = cp.getboolean(section, 'debug')
    LOG_ROOT = cp.get(section, 'log_root')
    MONGODB_CONF = cp.get(section, 'mongodb_conf')
    LANGUAGE_CODE = cp.get(section, 'language_code')
    UPLOAD_FILE_ROOT = cp.get(section, 'upload_file_root')
    SITE_DOMAIN = cp.get(section, 'file_storage_domain_conf')
    DUOSHUO_SECRET = cp.get(section, 'duoshuo_secret')
    DUOSHUO_SHORT_NAME = cp.get(section, 'duoshuo_short_name')
    EMAIL_HOST_USER = cp.get(section, 'email_host_user')
    EMAIL_HOST_PASSWORD = cp.get(section, 'email_host_password')
    SERVER_EMAIL = EMAIL_HOST_USER
    blog_db_conf = re.split(r'[@:/]', cp.get(section, 'blog_db_conf'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': blog_db_conf[0],
            'PASSWORD': blog_db_conf[1],
            'HOST': blog_db_conf[2],
            'PORT': blog_db_conf[3],
            'NAME': blog_db_conf[4],
        },
    }

_load_config('blog', [os.path.join(BASE_DIR, 'dongblog.cfg')])

WEBSITE_NAME = u'降龙'
WEBSITE_DESC = u'记录生活与工作的点滴，分享旅行与技术的乐趣。'
SAYING = u'一切都会过去！'    # u'不相信自己的人，连努力的价值都没有。'
WEBSITE_URL = 'http://xianglong.me'
WEBSITE_KEYWORDS = u'python,django,tornado,vim,linux,javascript,web开发,工作经验,人生,感悟,骑行'
GEEKBLOG_VERSION = '1.4.2'

LIST_PER_PAGE = 8

ADMINS = (
    ('WuXianglong', 'wuxianglong098@gmail.com'),
)

MANAGERS = ADMINS

# date and datetime field formats
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
PUBLISH_DATE_FORMAT = '%Y-%m-%d'

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Shanghai'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = UPLOAD_FILE_ROOT

MEDIA_URL = UPLOAD_FILE_ROOT

STATIC_ROOT = '/var/app/enabled/blog-webfront/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dongblog.urls'

WSGI_APPLICATION = 'dongblog.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'jsi18n', 'locale'),
)


# template name mappings
TEMPLATE_NAMES = {
    '404': {'p': '404.html', 'm': 'mobile/m_404.html'},
    'index': {'p': 'index.html', 'm': 'mobile/m_index.html'},
    'detail': {'p': 'detail.html', 'm': 'mobile/m_detail.html'},
    'archive': {'p': 'archive.html', 'm': 'archive.html'},
    'about': {'p': 'about.html', 'm': 'about.html'},
    'link': {'p': 'link.html', 'm': 'link.html'},
}

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_MIDDLEWARE_SECONDS = 3600
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# pipeline settings
PIPELINE_ENABLED = not DEBUG

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_YUGLIFY_BINARY = '/usr/local/bin/yuglify'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'css/style.css',
            'css/tooltips.css',
        ),
        'output_filename': 'css/base.min.css',
    },
    'index': {
        'source_filenames': (
            'css/slider.css',
            'css/pagination.css',
        ),
        'output_filename': 'css/index.min.css',
    },
    'detail': {
        'source_filenames': (
            'css/colorbox.css',
            'ueditor/third-party/SyntaxHighlighter/shCoreDefault.css',
        ),
        'output_filename': 'css/detail.min.css',
    },
    'about': {
        'source_filenames': (
            'css/about.css',
        ),
        'output_filename': 'css/about.min.css',
    },
    'mobile': {
        'source_filenames': (
            'css/mobile.css',
            'ueditor/third-party/SyntaxHighlighter/shCoreDefault.css',
        ),
        'output_filename': 'css/mobile.min.css',
        'extra_context': {
            'media': 'screen',
        },
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'js/jquery-1.11.1.min.js',
            'js/jquery-ui.js',
            'js/geekblog.js',
            'js/tooltips.js',
        ),
        'output_filename': 'js/base.min.js',
    },
    'index': {
        'source_filenames': (
            'js/jquery.slider.min.js',
            'js/jquery.animation.easing.js',
            'js/modernizr.min.js',
            'js/jquery.ui.touch-punch.min.js',
            'js/jquery.pagination.js',
            'js/jquery.qrcode.js',
        ),
        'output_filename': 'js/index.min.js',
    },
    'detail': {
        'source_filenames': (
            'js/jquery.colorbox.js',
            'js/jquery.qrcode.js',
            # 'ueditor/third-party/SyntaxHighlighter/shCore.min.js',
        ),
        'output_filename': 'js/detail.min.js',
    },
    'about': {
        'source_filenames': (
            'js/jquery-1.11.1.min.js',
            'js/about.js',
        ),
        'output_filename': 'js/about.min.js',
    },
    'archive': {
        'source_filenames': (
            'js/archive.js',
        ),
        'output_filename': 'js/archive.min.js',
    },
    'mobile': {
        'source_filenames': (
            'js/jquery-1.11.1.min.js',
            # 'ueditor/third-party/SyntaxHighlighter/shCore.min.js',
            'js/mobile.js',
        ),
        'output_filename': 'js/mobile.min.js',
    },
}


# admin left navigation settings
LEFT_NAV_MODELS = {
    'blog': {
        'order': 1,
        'title': _('content management'),
        'models': [
            'catearticles.*',
            'blog.models.Category',
            'blog.models.Tag',
            'blog.models.Link',
            'blog.models.Slider',
            'blog.models.Photo',
            'blog.models.Comment',
        ],
        'app_label_order': {
            'catearticles': 1,
            'blog': 2,
        }
    },
    'auth': {
        'order': 2,
        'title': _('system management'),
        'models': [
            'usermanagement.*',
            'django.contrib.admin.models.LogEntry',
        ],
        'app_label_order': {
            'usermanagement': 1,
            'admin': 2,
        }
    },
}

ADMIN_LIST_PER_PAGE = 20

LOG_FILE = os.path.join(LOG_ROOT, 'info.log')
LOG_ERR_FILE = os.path.join(LOG_ROOT, 'error.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'detail': {
            'format': '%(levelname)s %(asctime)s %(name)s [%(module)s.%(funcName)s] %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'detail',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_FILE,
        },
        'err_file': {
            'level': 'ERROR',
            'formatter': 'detail',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_ERR_FILE,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'geekblog': {
            'handlers': ['console', 'file', 'err_file'] if DEBUG else ['file', 'err_file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}



