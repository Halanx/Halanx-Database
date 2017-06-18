from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.order_list),
    url(r'^(?P<pk>[0-9]+)', views.order_id),
    url(r'^(?P<pk>[0-9]+)/items', views.order_items),
    url(r'^user/(?P<pk>[0-9]+)', views.user_orders),
]









