from django.shortcuts import render,redirect
from buyer.models import*
from siteadmin.models import*
from seller.models import*
from django.contrib import messages
import datetime

# Create your views here.

def buyerregistration(request):
    return render(request,'buyerregistration.html')
def buyerregistrationAction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    gender=request.POST['gender']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    dob=request.POST['dob']
    user=buyerregistration_tb(name=name,address=address,phone=phone,gender=gender,country=country,username=username,password=password,dob=dob)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect("buyerregistration")
def updateprofile(request):
    buyer=request.session['id']
    buyer=buyerregistration_tb.objects.filter(id=buyer)
    return render(request,"edit.html",{'buyer':buyer})
def updateprofileAction(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    dob=request.POST['dob']
    phone=request.POST['phone']
    gender=request.POST['gender']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    buyer=buyerregistration_tb.objects.filter(id=id).update(name=name,address=address,dob=dob,phone=phone,gender=gender,country=country,username=username,password=password)
    return redirect("updateprofile")
def viewsellerproduct(request):
    buyer=request.session['id']
    buyer=addproduct_tb.objects.all()
    return render(request,"viewsellerproduct.html",{'buyer':buyer})
def addtocart(request,id):
    buyer=addproduct_tb.objects.filter(id=id)
    return render(request,"addtocart.html",{'buyer':buyer})
def cartAction(request):
    productid=request.POST['id']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    name=request.POST['name']
    shippingaddress=request.POST['shippingaddress']
    phonenumber=request.POST['phonenumber']
    buyerid=request.session['id']
    buyer=cart_tb(quantity=quantity,totalprice=totalprice,name=name,shippingaddress=shippingaddress,phonenumber=phonenumber,buyerid_id=buyerid,productid_id=productid)
    buyer.save()
    return redirect("viewsellerproduct")
def viewcart(request):
    buyer=cart_tb.objects.all()
    return render(request,"viewcart.html",{'buyer':buyer})
def deletecart(request,id):
    buyer=cart_tb.objects.filter(id=id).delete()
    return redirect("viewcart")
def placeorder(request):
    cartitems=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    for cid in cartitems:
        cartitem=cart_tb.objects.filter(id=cid)
        stock=cartitem[0].productid.stock
        quantity=cartitem[0].quantity
        shippingaddress=cartitem[0].shippingaddress
        phonenumber=cartitem[0].phonenumber
        totalprice=cartitem[0].totalprice
        productid=cartitem[0].productid
        buyerid=request.session['id']
        sellerid=cartitem[0].productid.sellerid
        if quantity>int(stock):
            messages.add_message(request,messages.INFO,"quantity is greater")
            return redirect("viewcart")
        else:
            order=order_tb(quantity=quantity,shippindaddress=shippingaddress,phonenumber=phonenumber,totalprice=totalprice,productid=productid,sellerid=sellerid,buyerid_id=buyerid,date=date,time=time)
            order.save()
            stocknew=int(stock)-quantity
            product=addproduct_tb.objects.filter(id=productid.id).update(stock=stocknew)
            cartitem.delete()
            messages.add_message(request,messages.INFO,"order placed successfully")
    return redirect("viewcart")
def viewbuyerorder(request):
    buyer=request.session['id']
    buyer=order_tb.objects.filter(buyerid=buyer)
    return render(request,"viewbuyerorder.html",{'buyer':buyer})
def cancel(request,id):
    buyer=order_tb.objects.filter(id=id).update(status="canceled")
    return redirect("viewbuyerorder")
def viewtrackingdetails(request,id):
    #buyer=request.session['id']
    buyer=tracking_tb.objects.filter(id=id)
    return render(request,"viewtrackingdetails.html",{'buyer':buyer})
def searchproduct(request):
    return render(request,"searchproduct.html")
def searchproductAction(request):
    searchproduct=request.POST['searchproduct']
    buyer=addproduct_tb.objects.filter(productname__istartswith=searchproduct)
    return render(request,"viewsellerproduct.html",{'buyer':buyer})
def searchcategory(request):
    category=addcategory_tb.objects.all()
    return render(request,"searchcategory.html",{'category':category})
def searchcategoryAction(request):
    category=request.POST['category']
    price=request.POST['price']
    buyer=addproduct_tb.objects.filter(price__gte=price,categoryid=category)
    return render(request,"viewsellerproduct.html",{'buyer':buyer})
        



















