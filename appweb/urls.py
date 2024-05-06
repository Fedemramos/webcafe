from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('gallery', gallery, name='gallery'),
    path('almuerzo/',almuerzo, name='almuerzo'),
    path('bebidas/',bebibas, name='bebidas'),
    path('desayuno/',desayuno, name='desayuno'),
    path('cafeteria/',cafeteria, name='cafeteria'),
    path('ensalada/',ensalada, name='ensalada'),
    path('postres/',postres, name='postres'),
]