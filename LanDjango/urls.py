from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),


    url(r'^home/', 'Views.views.home'),
    url(r'^seats/', 'Views.views.seats'),
    url(r'^tournaments/', 'Views.views.tournaments'),
    url(r'^mypages/', 'Views.views.mypages'),

    url(r'^login/', 'Views.views.login'),

    url(r'^queries/login', 'Views.queries.login'),
    url(r'^queries/logout', 'Views.queries.logout'),
    url(r'^queries/register', 'Views.queries.register'),
    url(r'^queries/pick_seat', 'Views.queries.pick_seat'),
    url(r'^queries/order_ticket', 'Views.queries.order_ticket'),

    url(r'^$', 'Views.views.home'),
)
