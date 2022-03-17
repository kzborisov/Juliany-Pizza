from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from juliany_pizza import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('juliany_pizza.home.urls')),
                  path('accounts/', include('juliany_pizza.authentication.urls')),
                  path('menu/', include('juliany_pizza.menu.urls')),
                  path('cart/', include('juliany_pizza.cart.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
