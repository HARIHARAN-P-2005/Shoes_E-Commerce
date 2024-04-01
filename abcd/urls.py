from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage),
    path('ind',views.index,name="ind"),
    path('Men',views.Men),
    path('women',views.women),
    path('About',views.About),
    path('view',views.view),
    path('Views',views.Views),
    path('Mencollection',views.Mencollection),
    path('Womencollection',views.Womencollection),
    path('Sportscollection',views.Sportscollection),
    path('Formalcollection',views.Formalcollection),
    path('purchase',views.purchase),
    path('Purchasenow',views.Purchasenow),
    path('Now',views.Now),
    path('add',views.add),
    path('to',views.to),
    path('cart',views.cart),
    path('shoe',views.shoe),
    path('formal',views.formal),





]