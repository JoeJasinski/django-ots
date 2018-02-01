from django.conf.urls import url
from . import views as creds_views

urlpatterns = [
    url(r'^$',
        creds_views.CreateCred.as_view(),
        name="create_creds"),
    url(r'^(?P<pk>[0-9A-Fa-f-]+)/link/',
        creds_views.ViewCredLink.as_view(),
        name="view_creds_link"),
    url(r'^(?P<pk>[0-9A-Fa-f-]+)/qr/',
        creds_views.ViewCredLinkQR.as_view(),
        name="view_creds_qr"),
    url(r'^(?P<pk>[0-9A-Fa-f-]+)/$',
        creds_views.ViewCred.as_view(),
        name="view_creds"),
]
