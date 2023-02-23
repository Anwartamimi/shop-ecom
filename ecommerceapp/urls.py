from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>', 
        views.show_product, name='product_detail'),
    path('cart/', views.show_cart , name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
