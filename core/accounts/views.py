from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .tasks import sendEmail
import time
import requests
# Create your views here.



def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

def test(request):
    response = requests.get("https://914df9c0-90ab-43e3-b470-085908c96b27.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())