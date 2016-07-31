from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from pages import urls as pages_urls
from blog import urls as blog_urls


urlpatterns = [
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^', include(pages_urls, 'pages')),
    url(r'^', include(blog_urls, 'blog')),
    url(r'^', include(wagtail_urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)