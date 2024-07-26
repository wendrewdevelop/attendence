from django.urls import path
from .views import (
    IndexView, 
    SuccessView, 
    WontGoView,
    redirect_to_tunnel
)


urlpatterns = [
    path(
        '', 
        IndexView.as_view(),
        name='index'
    ),
    path(
        'success/', 
        SuccessView.as_view(),
        name='success'
    ),
    path(
        'wontgo/', 
        WontGoView.as_view(),
        name='wontgo'
    ),
    path(
        'tunnel/', 
        redirect_to_tunnel, 
        name='redirect_to_tunnel'
    ),
]