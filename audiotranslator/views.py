import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
import boto3

# Create your views here.
def root(request):
    return HttpResponse("ok")


@api_view(["POST"])
def convert(request):
    languageCode = None
    voiceId = None
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
    session = boto3.Session(region_name='us-east-1')
    lambdavar = session.client(service_name='lambda', use_ssl=True, region_name='us-east-1')
    response = lambdavar.invoke(
            FunctionName='ProjectLambda',
            InvocationType="RequestResponse",
            Payload=json.dumps(body)
        )
    audioFile = json.loads(response['Payload'].read().decode("utf-8"))
    return Response({"audio_file": audioFile}, status=status.HTTP_200_OK)
