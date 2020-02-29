
from django.urls import path

from cart import views

urlpatterns = [

	path('additem/<int:pid>/',views.additem, name='additem'),
	path('cartdetails/',views.cartdetails, name='cartdetails')
]