from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

#from search.views import search_page

urlpatterns = [
    # url(r'^$', home_page, name='home'),
    # url(r'^about/$', about_page, name='about'),
    # url(r'^contact/$', contact_page, name='contact'),
    url(r'^products/', include("products.urls", namespace='products')),
    # url(r'^food/', include("food.urls", namespace='food')),
    # url(r'^beverage/', include("beverage.urls", namespace='beverage')),
    #url(r'^search/$', search_page, name='search'),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)