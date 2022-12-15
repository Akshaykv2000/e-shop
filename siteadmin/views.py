from django.shortcuts import render,redirect
from siteadmin.models import*
from seller.models import*
from buyer.models import*
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    buyer=buyerregistration_tb.objects.filter(username=username,password=password)
    seller=sellerregistration_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,"adminhome.html")
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request,"buyerhome.html")
    elif seller.count()>0:
        status=seller[0].status
        if status=="approved":
            request.session['id']=seller[0].id
            return render(request,"sellerhome.html")
        else:
            messages.add_message(request,messages.INFO,"waiting for approval")
            return redirect("login")
    else:
        messages.add_message(request,messages.INFO,"incorrect username or password")
        return redirect("login")
def viewseller(request):
    admin=request.session['id']
    seller=sellerregistration_tb.objects.all()
    return render(request,'viewseller.html',{'seller':seller})
def approve(request,id):
    seller=sellerregistration_tb.objects.filter(id=id).update(status="approved")
    return redirect("viewseller")
def reject(request,id):
    seller=sellerregistration_tb.objects.filter(id=id).update(status="rejected")
    return redirect("viewseller")
def addcategory(request):
    return render(request,"addcategory.html")
def addcategoryAction(request):
    name=request.POST['name']
    add=addcategory_tb(name=name)
    add.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect("addcategory")
def checkusername(request):
    username=request.GET['username']
    admin=admin_tb.objects.filter(username=username)
    buyer=buyerregistration_tb.objects.filter(username=username)
    seller=sellerregistration_tb.objects.filter(username=username)
    if len(admin)>0:
        msg="exist"
    elif len(buyer)>0:
        msg="exist"
    elif len(seller)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

def forgotpassword(request):
    return render(request,"forgotpassword.html")
def forgotpasswordAction(request):
    username=request.POST['username']
    seller=sellerregistration_tb.objects.filter(username=username)
    buyer=buyerregistration_tb.objects.filter(username=username)
    if seller.count()>0:
        return render(request,"newpassword.html",{'data':username})
    elif buyer.count()>0:
        return render(request,"newpassword.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"incorrect username")
    return redirect("forgotpassword")
def newpasswordAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    username=request.POST['username']
    seller=sellerregistration_tb.objects.filter(name=name,dob=dob,country=country,username=username)
    buyer=buyerregistration_tb.objects.filter(name=name,dob=dob,country=country,username=username)
    if seller.count()>0:
        return render(request,"enternewpassword.html",{'data':username})
    elif buyer.count()>0:
        return render(request,"enternewpassword.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"added new password successfully")
    return redirect("login")
def enternewpasswordAction(request):
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.POST['username']
    if newpassword == confirmpassword:
        seller=sellerregistration_tb.objects.filter(username=username)
        buyer=buyerregistration_tb.objects.filter(username=username)
        if seller.count()>0:
            request.session['id']=seller[0].id
            sellerid=request.session['id']
            seller=sellerregistration_tb.objects.filter(id=sellerid).update(password=newpassword)
        else:
            request.session['id']=buyer[0].id
            buyerid=request.session['id']
            buyer=buyerregistration_tb.objects.filter(id=buyerid).update(password=newpassword)
        messages.add_message(request,messages.INFO,"password updated successfully")
        request.session.flush()
        return redirect("index")
    else:
        
        return redirect("login")
        













