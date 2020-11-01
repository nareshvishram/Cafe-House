from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .form import *
from django.utils import timezone

# Create your views here.
def Home(request):
    items = Item.objects.all().order_by("day")
    about = About.objects.last
    user=User.objects.filter(username=request.user.username)
    print("auth", request.user.is_authenticated)
    dict = {
        "items": items, "about": about,
    }
    return render(request, "index.html", dict)

def Login(request):
    error = None
    about = About.objects.last
    company = Company_Details.objects.last
    if request.method == "POST":
        data = request.POST
        un = data["un"]
        ps = data["ps"]
        usr = authenticate(request,username=un, password=ps)
        if usr != None:
            login(request,usr)
            return redirect("home")
        error = True
    dict = {
        "error": error, "about": about, "company": company
    }
    return render(request, "login.html", dict)


def Register(request):
    error=None
    about = About.objects.last
    company = Company_Details.objects.last
    if request.method == "POST":
        data = request.POST
        un = data["un"]
        ps = data["ps"]
        email = data["email"]
        already_exist=User.objects.filter(username=un)
        if not already_exist:
                first_name = data["first_name"]
                last_name = data["last_name"]
                usr = User.objects.create_user(username=un, email=email, password=ps)
                if usr!=None:
                        usr.first_name = first_name
                        usr.last_name = last_name
                        usr.save()
                        return redirect("login")
        error=True
    dict = {
        "about": about, "company": company,"error":error
    }

    return render(request, "register.html",dict)


def AdminPage(request):
    all_items = Item.objects.all()
    all_users=User.objects.all().order_by("-id")
    dict = {
        "all_items": all_items,"all_users":all_users
    }
    return render(request, "admin.html", dict)


def AboutEdit(request):
    about = About.objects.all().order_by("-id")
    about_all_data = About.objects.all()
    data = about[0]
    print("about", about)
    form = About_Edit_Form(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect("home")

    dict = {
        "about": form, "about_all_data": about_all_data
    }
    return render(request, "about_edit.html", dict)


def DeleteNote(request, note_id):
    About.objects.get(id=note_id).delete()
    return HttpResponse("deleted Successfully")


def Menu(request):
    about = About.objects.last
    items = Item.objects.all().order_by("day")
    dict = {
        "about": about, "items": items
    }
    return render(request, "menu.html", dict)


def TodaySpecial(request):
    about = About.objects.last
    item = Item.objects.all().order_by("day")
    day=timezone.now().weekday()
    special=Item.objects.filter(day=day).first
    next_day=(day+1)%5
    next_next_day=(day+2)%5
    nextday_special=Item.objects.filter(day=next_day).first
    nextnextday_special = Item.objects.filter(day=next_next_day).first
    print("day",day)
    dict = {
        "about": about, "items": item,"special":special,"next_day":nextday_special,"next_next_day":nextnextday_special
    }
    return render(request, "today_special.html", dict)


def EnterItem(request):
    form = Item_Model_Form()
    if request.method == "POST":
        form=Item_Model_Form(request.POST,request.FILES)
        if form.is_valid():
            data = form.save()
            print("dataaaaaaaaaaa",data)
            return redirect("home")
    dict = {
        "form": form
    }
    return render(request, "item_form.html", dict)


def EditItem(request, item_id):
    item = Item.objects.get(id=item_id)
    form = Item_Model_Form(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("home")
    dict={"form":form}
    print("bata",form.is_valid())
    return render(request, "item_form.html",dict)


def Order_Item(request,item_id):
    ordered_item=Item.objects.get(id=item_id)
    if request.method=="POST":
        data = request.POST
        freq = data["freq"]
        total=int(freq)
        return HttpResponse("<center>order is placing @@@@@ ..")
    dict={
        "ordered_item":ordered_item
    }
    return render(request,"order_item.html",dict)

def Order(request):
    pass
    if request.method=="POST":
        data=request.POST
        price=data["price"]
        name=data["name"]
        freq=data["freq"]
        data.save()

def Contact(request):
    about = About.objects.last
    company=Company_Details.objects.last
    if request.method=="POST":
        data=request.POST
        name=data["name"]
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        Contact_Data.objects.create(name=name,email=email,subject=subject,message=message)
    dict={
        "about":about,"company":company
    }
    return render(request,"contact.html",dict)


def Received_Messages(request):
    data=Contact_Data.objects.all().order_by("-id")
    dict={
        "data":data
    }
    return render(request,"received_messages.html",dict)

def Logout(request):
    logout(request)
    return redirect("home")