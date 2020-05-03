from django.shortcuts import render

def messages(request):      #messages = index
    return render(request, 'chat/index.html')