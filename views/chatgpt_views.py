from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.utils import timezone

def ask_openai(message):
    response = openai.ChatCompletion.create(
        # model = "gpt-4",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user.id)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user='testuser', message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})