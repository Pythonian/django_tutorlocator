from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('login/',
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True), name='login'),

    # # Registration
    # path('tutor/signup/', views.tutor_signup, name='tutor_signup'),
    path('signup/', views.signup, name='signup'),

    # # Customer account
    # path('profile/', views.profile, name='profile'),
    # path('profile/orders/', views.customer_orders, name='orders'),
    # path('profile/addresses/', views.customer_addresses, name='addresses'),
    # path('profile/wishlists/', views.customer_wishlist, name='wishlist'),

    # # Vendor account
    # path('vendors/', views.vendors, name='vendors'),
    # path('vendor/', views.vendor_account, name='vendor'),
    # path('vendor/orders/', views.vendor_orders, name='vendor_orders'),
    # path('vendor/products/', views.vendor_products, name='vendor_products'),
    # path('vendor/<str:username>/',
    #      views.vendor_profile, name='vendor_profile'),

    # path('deactivate/', views.deactivate, name='deactivate'),
]
