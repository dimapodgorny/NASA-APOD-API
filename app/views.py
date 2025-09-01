from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .services import get_apod
from datetime import date
from colorama import Fore, Style 

def apod_page(request, params: dict = {}):
    context = {}
    
    if request.method == "POST":
        if request.POST.get("custom_apod_date"):
            params["date"] = request.POST.get("custom_apod_date")
        
        try:
            data : dict = get_apod(params)
            
            request.session["apod_data"] = data
        except Exception as e:
            print(Fore.RED + "error: " + str(e) + Style.RESET_ALL)
            context["error"] = str(e)
            request.session["apod_error"] = str(e)
        
        return redirect("apod_page")
    
    context = {
        'apod': request.session.pop('apod_data', None),
        'error': request.session.pop('apod_error', None)
    }

    
    return render(request,  "apod.html", context)