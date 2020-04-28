from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('addStock/',views.addStock,name='addStock'),
    path('delete/<ticker_id>',views.delete,name='delete'),
    path('deleteStock/', views.deleteStock,name='deleteStock'),
]
