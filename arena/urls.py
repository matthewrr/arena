from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from arena.views import SignUpView, validate_username

#from search.views import search_page

urlpatterns = [
    # url(r'^$', home_page, name='home'),
    # url(r'^about/$', about_page, name='about'),
    # url(r'^contact/$', contact_page, name='contact'),
    url(r'^products/', include("products.urls", namespace='products')),
    #url(r'^search/$', search_page, name='search'),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)