from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns = [
    path('spe1/',spe1,name='spe1'),
    path('spe2/',spe2,name='spe2'),
]