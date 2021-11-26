from math import ceil

from django.shortcuts import render
from .models import Product, Contacts, Order


def test(request):
    products = Product.objects.all()
    params = {"Product": products}
    return render(request, "shop/test.html", params)


def index(request):

    all_products = []
    categories = list(set(Product.objects.all().values_list('category', flat=True)))
    categories.sort()

    cards_per_row = 1
    for cat in categories:
        products = Product.objects.filter(category=cat)
        n = len(products)
        number_of_slides = n // cards_per_row + ceil((n / cards_per_row) - (n // cards_per_row))
        all_products.append([products, range(1, number_of_slides), number_of_slides, cards_per_row])

    params = {'all_products': all_products}
    return render(request, "shop/index.html", params)


def about_us(request):
    return render(request, "shop/about.html")


def contact_us(request):
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def product_view(request, this_id):
    product = Product.objects.filter(id=this_id)

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contacts(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, "shop/productView.html", {"product": product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + ' ' + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()

        thank = True
        id = order.order_id

        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})

    return render(request, "shop/checkout.html")
