from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('records/', index, name='records'),
    path('records/search/result/', search_record, name='search_record'),
    path('records/add/', add_record, name='add_record'),
    path('records/<int:pk>/edit/', edit_record, name='edit_record'),
    path('records/<int:pk>/delete/', delete_record, name='delete_record'),
]
