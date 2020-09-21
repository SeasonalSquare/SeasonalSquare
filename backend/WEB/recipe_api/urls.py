from django.urls import path
from . import views

app_name = 'recipe_api'

urlpatterns = [
    path('grocery/<str:grocery_name>/', views.grocery, name='grocery'),
    path('<int:recipe_pk>/', views.recipe, name='recipe'),
]
