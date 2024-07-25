from django.urls import path
from .views import (
    IndexView, 
    SuccessView, 
    WontGoView
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
    )
]