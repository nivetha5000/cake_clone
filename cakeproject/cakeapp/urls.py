from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('birthday/',views.birthday, name='birthday'),
    path('cart2/',views.cart2, name='cart2'),
    path('contact/',views.contact, name='contact'),
    path('cupcake/',views.cupcake, name='cupcake'),
    path('variety/',views.variety, name='variety'),
    path('wedding/',views.wedding, name='wedding'),
]