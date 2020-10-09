from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DeleteView


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"

#   def home(request):
#        context = {
#            'items': Item.objects.all()
#        }
#        return render(request, "home-page.html", context)


#def home(request):
    #return render(request, "checkout.html")
