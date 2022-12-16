from django.urls import path
from.views import Homepageview,PostDetailview


app_name = 'mbts'

urlpatterns = [
    path('',Homepageview.as_view(),name='index'),
    path('detail/<int:pk>/',PostDetailview.as_view(),name='detail')
]