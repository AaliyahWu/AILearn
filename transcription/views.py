# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
# def transcribe(request):
#     transcript = request.POST.get('transcript')
#     # 在這裡處理 transcript...
#     return JsonResponse({'status': 'ok'})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transcription
import json

@csrf_exempt
def transcribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        transcript = data.get('transcript')

        Transcription.objects.create(text=transcript)

        return JsonResponse({"message": "Transcription saved successfully."})

    else:
        return JsonResponse({"message": "Invalid request method."})


