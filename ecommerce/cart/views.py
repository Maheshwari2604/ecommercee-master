# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import product
from django.shortcuts import render

# Create your views here.
def view(request):
    try:
        the_id = request.session['cart_Id']
    except:
        the_id = None
        products = product.objects.all()
        message = "Please do shoping, you have nothing in your cart"
        context = {"empty": True, "message": message, "products": products}
        return render(request, 'carts/view.html', context)

    if the_id:
        products = product.objects.all()
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart, "products": products}    
    else:
        products = product.objects.all()
        message = "Please do shoping, you have nothing in your cart"
        context = {"empty": True, "message": message, "products": products}
    #template = "cart/view.html"
    return render(request, 'carts/view.html', context) 


def cart_update(request, slug):
    #return HttpResponse(slug)
    request.session.set_expiry(300)
    print "hey"
    qty = request.GET.get('qty')
    try:
        if qty is not None: 
            update_qty = True
            print "hey u r in try block"
            print qty
        else:
            qty = None
            update_qty = False
            print "none hai"
    except:
        print "hey none"

    try:
        the_id = request.session['cart_Id']
    except:
        new_item = carttotal()
        new_item.save()
        request.session['cart_Id'] = new_item.id
        the_id = new_item.id
        print the_id

    cart = carttotal.objects.get(id=the_id)
    #return render(request, 'cart/result.html', context)
    #print "hello"
    #context = {"cart":cart }
    try:
        prod = product.objects.get(slug=slug)
        #return HttpResponse(products)
    except:
        pass

    cart_item, created = cartitem.objects.get_or_create(cart=cart, product=prod)

#    if not cart_item in cart.item.all():
#        cart.item.add(cart_item)
#    else:
#          cart.item.remove(cart_item)    

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass


    #item_sub_price = item.product.price
  
    new_item = 0.00
    for item in cart.cartitem_set.all():
        totalitem = float(item.product.price) * item.quantity
        new_item += totalitem

    request.session['item_total'] = cart.cartitem_set.count()
    #print cart.products.count()
    cart.Total = new_item
    cart.save()    

    #return HttpResponseRedirect(reverse("home")) 

    return HttpResponseRedirect(reverse("view"))


'''
    if not prod in cart.products.all():
        cart.products.add(prod)
    else:
        cart.products.remove(prod)  
'''