"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from siteadmin import views as adminview
from seller import views as sellerview
from buyer import views as buyerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name='index'),
    path('buyerregistration/',buyerview.buyerregistration,name="buyerregistration"),
    path('buyerregistrationAction/',buyerview.buyerregistrationAction,name="buyerregistrationAction"),
    path('sellerregistration/',sellerview.sellerregistration,name="sellerregistration"),
    path('sellerregistrationAction/',sellerview.sellerregistrationAction,name="sellerregistrationAction"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('viewseller/',adminview.viewseller,name="viewseller"),
    path('approve<int:id>/',adminview.approve,name="approve"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('addcategory/',adminview.addcategory,name="addcategory"),
    path('addcategoryAction/',adminview.addcategoryAction,name="addcategoryAction"),
    path('checkusername/',adminview.checkusername,name="checkusername"),
    path('updateprofile/',buyerview.updateprofile,name="updateprofile"),
    path('updateprofileAction/',buyerview.updateprofileAction,name="updateprofileAction"),
    path('editseller/',sellerview.editseller,name="editseller"),
    path('editsellerAction/',sellerview.editsellerAction,name="editsellerAction"),
    path('addproduct/',sellerview.addproduct,name="addproduct"),
    path('addproductAction/',sellerview.addproductAction,name="addproductAction"),
    path('viewaddedproduct/',sellerview.viewaddedproduct,name="viewaddedproduct"),
    path('delete<int:id>/',sellerview.delete,name="delete"),
    path('edit<int:id>/',sellerview.edit,name="edit"),
    path('editproductAction/',sellerview.editproductAction,name="editproductAction"),
    path('viewsellerproduct/',buyerview.viewsellerproduct,name="viewsellerproduct"),
    path('addtocart<int:id>/',buyerview.addtocart,name="addtocart"),
    path('cartAction/',buyerview.cartAction,name="cartAction"),
    path('viewcart/',buyerview.viewcart,name="viewcart"),
    path('deletecart<int:id>/',buyerview.deletecart,name="deletecart"),
    path('placeorder/',buyerview.placeorder,name="placeorder"),
    path('viewbuyerorder/',buyerview.viewbuyerorder,name="viewbuyerorder"),
    path('vieworder/',sellerview.vieworder,name="vieworder"),
    path('orderapprove<int:id>/',sellerview.orderapprove,name="orderapprove"),
    path('orderreject<int:id>/',sellerview.orderreject,name="orderreject"),
    path('cancel<int:id>/',buyerview.cancel,name="cancel"),
    path('trackingdetails<int:id>/',sellerview.trackingdetails,name="trackingdetails"),
    path('trackingdetailsAction/',sellerview.trackingdetailsAction,name="trackingdetailsAction"),
    path('viewtrackingdetails<int:id>/',buyerview.viewtrackingdetails,name="viewtrackingdetails"),
    path('confirmcancellation<int:id>/',sellerview.confirmcancellation,name="confirmcancellation"),
    path('searchproduct/',buyerview.searchproduct,name="searchproduct"),
    path('searchproductAction/',buyerview.searchproductAction,name="searchproductAction"),
    path('searchcategory/',buyerview.searchcategory,name="searchcategory"),
    path('searchcategoryAction/',buyerview.searchcategoryAction,name="searchcategoryAction"),
    path('forgotpassword/',adminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',adminview.forgotpasswordAction,name="forgotpasswordAction"),
    path('newpasswordAction/',adminview.newpasswordAction,name="newpasswordAction"),
    path('enternewpasswordAction/',adminview.enternewpasswordAction,name="enternewpasswordAction")


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
