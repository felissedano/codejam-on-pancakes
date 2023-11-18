import json
from django.http import JsonResponse
from django.shortcuts import render
from . import mqtt_client

def read_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})