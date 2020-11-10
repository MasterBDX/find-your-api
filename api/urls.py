
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls',namespace='main')),
 
    # APIs urls combination
    path('api/users/', include('apis.users_api.urls')),
    path('api/posts/', include('apis.posts_api.urls')),
    path('api/comments/', include('apis.comments_api.urls')),
    path('api/blog/', include('apis.blog_api.urls')),
]




if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)