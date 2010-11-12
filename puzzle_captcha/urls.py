from django.conf.urls.defaults import *

urlpatterns = patterns('puzzle_captcha.views',
    (r'^$', 'render_puzzle'),
)
