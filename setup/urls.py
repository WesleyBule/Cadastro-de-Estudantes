
from django.contrib import admin
from django.urls import path
from crud.views import EstudanteListView ,EstudanteCreateView ,EstudanteUpdateView , EstudanteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EstudanteListView.as_view(), name="estudante_list"),
    path('create', EstudanteCreateView.as_view(),name="estudante_create"),
    path('update/<int:pk>',EstudanteUpdateView.as_view(),name="estudante_update"),
    path('delete/<int:pk>', EstudanteDeleteView.as_view(), name="estudante_delete")
    x
]
