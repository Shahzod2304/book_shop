from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView, DetailView,View
from .models import *
# Create your views here.
class HomePage(ListView):
    model = Book
    template_name = 'home.html'

class AddProducts(DetailView):
    model = Book
    template_name = "addproduct.html"

class NewsPageView(ListView):
    model = NewsPageModel
    template_name = 'news_page_list.html'

class NewsPageDetail(DetailView):
    model = NewsPageModel
    template_name = 'news_page_detail.html'

class AddToCartView(TemplateView):
    template_name = 'addtocart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['pro_id']
        product_obj = Book.objects.get(id=product_id)

        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.price
                cartproduct.save()
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj,rate = product_obj.price,quantity=1,subtotal=product_obj.price)
                cart_obj.total += product_obj.price
                cart_obj.save()
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj,rate = product_obj.price,quantity=1,subtotal=product_obj.price)
            cart_obj.total += product_obj.price
            cart_obj.save()
        return context


class MyCartView(TemplateView):
    template_name = "mycart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context



class ManageCartView(View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart

        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("mycart")

class EmptyCartView(View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("mycart")

class AksiyaPage(ListView):
    model = Aksiya
    template_name = 'aksiyapage.html'


class AksiyaPageDetail(DetailView):
    model = Aksiya
    template_name = 'news_page_detail.html'