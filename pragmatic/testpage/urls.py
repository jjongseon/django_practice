
from django.urls import path
from testpage.views import testpage
app_name = 'testpage'

urlpatterns = [
    path('', testpage, name='testpage'),

]