from django.conf.urls.defaults import *

urlpatterns = patterns('test_app.views',
    (r'^$', 'show_form'),
)
