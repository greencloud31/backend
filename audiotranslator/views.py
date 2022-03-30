import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status

# Create your views here.
def root(request):
    return HttpResponse("ok")


@api_view(["POST"])
def convert(request):
    body = json.loads(request.body.decode("utf-8"))
    if "text" not in body or "language" not in body:
        return Response(
            {
                "error": [
                    "Missing required fields text, language."
                ]
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(
            {
                "text": body["text"],
                "language": body["language"]
            },
            status=status.HTTP_200_OK,
        )
