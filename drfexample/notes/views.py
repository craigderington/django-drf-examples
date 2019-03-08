from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import Note, NoteTag, NoteReminder
from .serializers import NoteSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def note_list(request):
    """
    List all notes
    :param request
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def note_detail(request, note_pk_id):
    """
    Retrieve, update or delete a note.
    :param request
    :param pk
    """
    try:
        note = Note.objects.get(pk=note_pk_id)

        if request.method == 'GET':
            serializer = NoteSerializer(note)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = NoteSerializer(note, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            note.delete()
            return HttpResponse(status=204)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)
