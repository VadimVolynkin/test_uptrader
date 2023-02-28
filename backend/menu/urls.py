from django.urls import path
from menu.views import get_page, get_pages

app_name = 'menu'

urlpatterns = [
    path('', get_pages, name='page_list'),
    path('<slug:slug>/', get_page, name='page_detail'),
]
