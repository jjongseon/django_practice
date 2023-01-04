
from django.urls import path

from searchapp.views import hello_world

app_name = 'searchapp'

urlpatterns = [
    path("hello_world/", hello_world, name='hello_world'),

]