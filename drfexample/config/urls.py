from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from .views import api_root

schema_view = get_swagger_view(title='Snippet API')

# url list
urlpatterns = [
    path('', api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view),
    path('bookmarks/', include('bookmarks.urls')),
    path('snippets/', include('snippets.urls')),
    path('users/', include('users.urls')),
    path('locations/', include('locations.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls))
    ]
