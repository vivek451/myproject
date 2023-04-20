from django.urls import path

from . import views


urlpatterns = [
    path(route='list/', view=views.MyModelListView.as_view(), name='my_model_list'),
    path(route='create/', view=views.MyModelCreateView.as_view(), name='my_model_create'),
    path('<int:pk>/update/', view=views.MyModelUpdateView.as_view(), name='my_model_update'),
]