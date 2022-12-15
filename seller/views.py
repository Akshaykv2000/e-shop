from django.shortcuts import render,redirect
from seller.models import*
from buyer.models import*
from siteadmin.models import*
from django.contrib import messages
import datetime

# Create your views here.
def sellerregistration(request):
    return render(request,'sellerregistration.html')
def sellerregistrationAction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="no pic"
    username=request.POST['username']
    password=request.POST['password']
    user=sellerregistration_tb(name=name,address=address,phone=phone,dob=dob,gender=gender,country=country,username=username,password=password,file=img)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect("sellerregistration")
def editseller(request):
    sellerid=request.session['id']
    seller=sellerregistration_tb.objects.filter(id=sellerid)
    return render(request,"editseller.html",{'seller':seller})
def editsellerAction(request):
   
    sellerid=request.POST['id']
    seller=sellerregistration_tb.objects.filter(id=sellerid)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    username=request.POST['username']
    country=request.POST['country']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=seller[0].file
    password=request.POST['password']
    seller=sellerregistration_tb.objects.filter(id=sellerid).update(name=name,address=address,gender=gender,dob=dob,phone=phone,username=username,country=country,password=password)
    seller_object=sellerregistration_tb.objects.get(id=sellerid)
    seller_object.file=file
    seller_object.save()
    return render(request,"editseller.html",{'seller':seller})
def addproduct(request):
    category=addcategory_tb.objects.all()
    return render(request,'addproduct.html',{'category':category})
def addproductAction(request):
    productname=request.POST['productname']
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    category=request.POST['category']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="no pic"
    sellerid=request.session['id']
    seller=addproduct_tb(productname=productname,price=price,stock=stock,details=details,categoryid_id=category,sellerid_id=sellerid,file=img)
    seller.save()
    messages.add_message(request,messages.INFO,"product added successfully")
    return redirect("addproduct")
def viewaddedproduct(request):
    sellerid=request.session['id']
    product=addproduct_tb.objects.filter(sellerid=sellerid)
    return render(request,'viewaddedproduct.html',{'product':product})
def delete(request,id):
    product=addproduct_tb.objects.filter(id=id).delete()
    return redirect("viewaddedproduct")
def edit(request,id):
    product=addproduct_tb.objects.filter(id=id)
    category=addcategory_tb.objects.all()
    return render(request,"editproduct.html",{'product':product,'category':category})
def editproductAction(request):
    productid=request.POST['id']
    product=addproduct_tb.objects.filter(id=productid)
    productname=request.POST['productname']
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    print(details)
    category=request.POST['category']
    print(category)
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=product[0].file
    sellerid=request.session['id']
  
    product_object=addproduct_tb.objects.get(id=productid)
    product_object.file=file
    product_object.save()
    seller=addproduct_tb.objects.filter(id=productid).update(productname=productname,price=price,stock=stock,details=details,categoryid_id=category)
    return redirect("viewaddedproduct")
def vieworder(request):
    seller=request.session['id']
    seller=order_tb.objects.filter(sellerid=seller)
    return render(request,"vieworder.html",{'seller':seller})
def orderapprove(request,id):
    seller=order_tb.objects.filter(id=id).update(status="approved")
    return redirect("vieworder")
def orderreject(request,id):
    seller=order_tb.objects.filter(id=id).update(status="rejected")
    return redirect("vieworder")
def trackingdetails(request,id):
    seller=order_tb.objects.filter(id=id)
    return render(request,"trackingdetails.html",{'seller':seller})
def trackingdetailsAction(request):
    orderid=request.POST['id']
    print(orderid)
    #ordert=order_tb.objects.filter(id=orderid)
    #print(ordert)
    details=request.POST['details']
    print(details)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    seller=tracking_tb(orderid_id=orderid,details=details,time=time,date=date)
    seller.save()
    #order=order_tb.objects.filter(id=orderid)
    #return render(request,"trackingdetails.html",{'seller':seller})
    return redirect("vieworder")
def confirmcancellation(request,id):
    seller=order_tb.objects.filter(id=id)
    seller.update(status="confirm cancelled")
    quantity=seller[0].quantity
    stock=seller[0].productid.stock
    stock=int(stock)+quantity
    product=addproduct_tb.objects.filter(id=seller[0].productid.id)
    product.update(stock=stock)
    return redirect("vieworder")
    
    











    
