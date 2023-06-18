from django.urls import path, include
from django_plant.web.views import create_profile, show_home, edit_profile, details_profile, delete_profile, \
    create_plant, delete_plant, edit_plant, details_plant, show_catalogue

urlpatterns = (
    path('', show_home, name='index'),
    path('catalogue/', show_catalogue, name="catalogue"),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('create/', create_plant, name='create plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
    path('edit/<int:pk>', edit_plant, name='edit plant'),
    path('details/<int:pk>', details_plant, name='details plant'),
)
