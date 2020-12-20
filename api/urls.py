
from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap

from django.conf import settings
from django.conf.urls.static import static

from api.sitemaps import GuidesSitemap,StaticSitemap

import debug_toolbar

sitemaps = {'guides':GuidesSitemap,
            'static':StaticSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('admin/defender/', include('defender.urls')), # defender admin
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    
    path('', include('main.urls',namespace='main')),
 
    # APIs urls combination
    path('api/users/', include('apis.users_api.urls',namespace='users')),
    path('api/posts/', include('apis.posts_api.urls',namespace='posts')),
    path('api/comments/', include('apis.comments_api.urls',namespace='comments')),
    path('api/blog/', include('apis.blog_api.urls',namespace='blog')),
]




if settings.DEBUG == True:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)