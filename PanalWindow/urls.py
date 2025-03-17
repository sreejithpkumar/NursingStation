from django.urls import path
from . import views


urlpatterns = [
    path('fullinfo/',views.Details),
    path('edit/<keyid>', views.Edit),
    path('delete/<keyid>',views.Delete)
]