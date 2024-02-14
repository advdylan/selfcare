from django.urls import path
from . import views
from patients.helpers import UserAutoComplete, UserAutocomplete

from patients import helpers

urlpatterns = [

    path("", views.index, name="index"),
    path('upload_images', views.upload_images, name="upload_images"),
    path('upload_files', views.upload_files, name='upload_files'),
    path('add_permission', helpers.add_permission, name="add_permission"),
    path('api/user-autocomplete/', UserAutoComplete.as_view(), name='user-autocomplete'),
    path('autocomplete/user/$', views.autocomplete_user, name='autocomplete_light:user-autocomplete')
]