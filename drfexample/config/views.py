from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'bookmarks': reverse('bookmark-list', request=request, format=format),
        'locations': reverse('location-list', request=request, format=format),
        'todos': reverse('todo-list', request=request, format=format),
    })
