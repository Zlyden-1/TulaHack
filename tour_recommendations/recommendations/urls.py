from . import views
from django.urls import path


urlpatterns = [
    path('', views.UnloggedEventsListView.as_view(), name='index')

]
