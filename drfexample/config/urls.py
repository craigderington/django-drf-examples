from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Snippet API')

# url list
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view),
    path('bookmarks/', include('bookmarks.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls))
    ]
