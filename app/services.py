from django.http import JsonResponse, HttpResponse
import requests
from decouple import config


    

def get_apod(params: dict = {}):
    url = "https://api.nasa.gov/planetary/apod"
    params["api_key"] = config("NASA_API_KEY")
    
    response = requests.get(url, params=params)    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()