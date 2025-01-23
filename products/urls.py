from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  
    path('login/', views.login_page, name='login_page'),
    path('Register/', views.register_page, name='register_page'),
    path('loggedin/', views.login_user, name='login'),
    path('signedup/', views.signup_page, name='signup_page'),
    path('logout/', views.logout_user, name='logout'),
    path('cancellationreturn/', views.cancellation_return, name='cancellation_return'),
    path('privacypolicy/', views.privacy_policy, name='privacy_policy'),
    path('termsofuse/', views.terms_of_use, name='terms_of_use'),
    path('contactus/', views.contact_us, name='contact'),
    path("chatbot/", views.chatbot, name="chatbot"),
    path('aboutus/', views.aboutus_page, name='aboutus_page'), 
    path('bookappointment/', views.book_appointment, name='book_appointment'),
    path('cancelorder/<int:product_id>/<int:quantity>/', views.cancel_order, name='cancel_order'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('deleteorder/<int:product_id>/', views.delete_order, name='delete_order'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('blog/', views.blog_page, name='blog_page'),  
    path('products/', views.product_list, name='product_list'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('orders/', views.order_confirmation, name='order_confirmation'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('get-cart-count/', views.get_cart_count, name='get_cart_count'),
    path('blog/<int:product_id>/', views.single_blog, name='single_blog'),


]
