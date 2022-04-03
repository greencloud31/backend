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
    session = boto3.Session(aws_access_key_id="ASIARVAB6G2YZPGBR2GQ",
                            aws_secret_access_key="wD+W0LvQbgMlL2989t3uS+xBakN/DpSBjUZlIR98",
                            aws_session_token="FwoGZXIvYXdzEMb//////////wEaDElJBZ6UCG0QQ5hVSyLAAVZERrH0zRxwVW0R5eqa/KQTviPxVH00BQXHeqE9z9N1N0GtMEQwhFKO23bKvyP8PVpaDK4u3YzThn3bidt7LUdSFlCRDzMxzHcvrUsOM4D1iSPFUOmvE6dAlgzXf3IGdfZG+u2apYNLDD7ZP6VPwBNNLwhpHbVaGJuVV5Z77Gk32C1gmbp2JFKUizC7v4kcKI++J5lYs6BZeWMiRomPR7M8jKh9+Ani9vPzYZlGoausbcs6yjJsiJ0RqRnv6UZc/CjF46KSBjIt1G7sJEyvqqQXybECMalBpLGkyihtYQf+DnQqL6QOjoW5tGNQH/S/NENFKmto",
                            region_name='us-east-1'
                            )
    lambdavar = session.client(service_name='lambda', use_ssl=True, region_name='us-east-1')
    response = lambdavar.invoke(FunctionName='ProjectLambda',
                                InvocationType="RequestResponse",
                                Payload= json.dumps(body)
                                )
    audioFile = json.loads(response['Payload'].read().decode("utf-8"))
    return Response(
            {
               "audio_file": audioFile
            },
            status=status.HTTP_200_OK,
        )
