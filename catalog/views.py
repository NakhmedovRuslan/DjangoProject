from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'main.html')

def contact_view(request):
    if request.method == "GET":
        return render(request, 'contacts.html')

def submit_form(request):
    if request.method == 'POST':
        html_content = """
        <html>
        <body>
        <h1>Спасибо за обратную связь!</h1>
        </body>
        </html>
        """
        return HttpResponse(html_content)

    else:
        return render(request, 'contacts.html')


