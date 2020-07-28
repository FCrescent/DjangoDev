
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
         #"index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title':"Hello Django",
            'message': "Hello Django!",
            'content': " on this great date and time >>> " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )



#ANOTHER OLD CODE 
#from datetime import datetime
#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "<br>With Django Version: 1.11.29 AND Python Version: 3.6.6 (connu grâce à erreur de test :) )"
#    html_content += "</body></html>"
#    return HttpResponse(html_content) 
    
    #return HttpResponse("Hello, Django! (& World ?)") #This is another Old line of code 


#BELOW is Old Code (first code)
#from django.shortcuts import render

# Create your views here.
