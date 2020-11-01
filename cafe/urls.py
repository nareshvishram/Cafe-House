"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cafeHouse.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('login/',Login,name="login"),
    path('register/',Register,name="register"),
    path('adminPage/',AdminPage,name="admin_page"),
    path('aboutEdit/',AboutEdit,name="aboutEdit"),
    path('deleteAboutNote/<int:note_id>/',DeleteNote,name="deleteNote"),
    path('menu/',Menu,name="menu"),
    path('todatSpecial/',TodaySpecial,name="todaySpecial"),
    path('enterItem/',EnterItem,name="enterItem"),
    path('editItem/<int:item_id>/',EditItem,name="editItem"),
    path("orderItem/<int:item_id>/",Order_Item,name="orderItem"),
    path('order/',Order,name="order"),
    path('contact/',Contact,name="contact"),
    path('receivedMessages/',Received_Messages,name="receivedMessages"),
    path('logout/',Logout,name="logout"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
