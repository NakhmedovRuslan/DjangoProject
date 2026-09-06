from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, "base.html")


def home_view(request):
    return render(request, "main.html")


def categories(request):
    return render(request, "categories.html")


def choose_category(request):
    return render(request, "choose_category.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html")


def submit_form(request):
    if request.method == "POST":
        html_content = """
        <html>
        <body>
        <h1>Спасибо за обратную связь!</h1>
        </body>
        </html>
        """
        return HttpResponse(html_content)

    else:
        return render(request, "contacts.html")


def home_view(request):
    products = Product.objects.all()

    return render(request, "main.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "product_detail.html", context)
