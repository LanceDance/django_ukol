from django.urls import path
from ukol import views

urlpatterns = [
    path("import/", views.import_data),
    path("detail/<str:name_of_model>/", views.detail_of_model),
    path("detail/<str:name_of_model>/<id>", views.detail_of_value),
]
