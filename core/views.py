from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItems, Order
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItems.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity is updated")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItems.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed to your cart")
            return redirect("core:product", slug=slug)
        else:
            # add a message saying the user dosent have an order
            messages.info(request, "This item is not in your cart")
            return redirect("core:product", slug=slug)
    else:
        # add a message saying the user dosent have an order
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


# #  def home(request):
#        context = {
#            'items': Item.objects.all()
#        }
#        return render(request, "home-page.html", context)


# def home(request):
#     return render(request, "checkout.html")
