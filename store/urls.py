
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),	
    path('register/', views.register, name="register"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('product_details/<str:id>/', views.productDetails, name="product_details"),

]