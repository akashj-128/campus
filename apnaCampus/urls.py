from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from admin_honeypot import views as honeypot_views

urlpatterns =[
    # Include admin honeypot URLs
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('apnaCampus/',admin.site.urls),
    path('', views.home, name ='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)