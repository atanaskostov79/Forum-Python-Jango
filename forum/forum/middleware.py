import requests
from django.conf import settings

from django.shortcuts import render, redirect

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.translations = "ala bala"

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # def process_response(self, request, response):
    #     response.content['count'] = self.translations
    #     return response
    def process_template_response(self, request, response):
        print("Mid dddddd" )
        response.content['count'] = self.translations
        return render(request, 'accounts/dashboard.html', {'count':"23sm"})

        # return response
