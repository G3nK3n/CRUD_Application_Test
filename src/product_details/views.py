from django.shortcuts import render
from .models import Details
from .forms import ProductForm
# Create your views here.

def product_create_view(request):
    context = {}
    return render(request, "product_form.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
    
#     context = {
#         'form': form
#     }
#     return render(request, "product_form.html", context)


def product_detail_view(request):
    obj = Details.objects.get(id=1)
    context = {
        'year': obj.year, 
        'name': obj.name, 
        'price': obj.price,
        'stock_number':obj.stock_number
    }
    return render(request, "prod_details.html", context)