import json
from django.http import JsonResponse
from . import mqtt_client

def publish_message(request):
    request_data = json.loads(request.body)
    # to fix the duplicate messages
    # rc, mid = mqtt_client.client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': request_data})