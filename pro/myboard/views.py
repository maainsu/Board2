from django.shortcuts import render
from myboard.models import Shopboard
from django.http.response import HttpResponseRedirect
from django.core.paginator import *
import socket
from datetime import datetime

# Create your views here.
def Main(request):
    return render(request, "main.html")

def showList(request):
    # 페이징 처리
    lists = Shopboard.objects.all().order_by("-num")
    paginator = Paginator(lists, 5)
    try:
        page = request.GET.get("page")
    except:
        page = 1
        
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, "showList.html", {"boardList":list})

def showContent(request):
    data = Shopboard.objects.get(num=request.GET.get("num"))
    print("변경전: ", data.readcnt)
    data.readcnt = data.readcnt+1
    data.save()
    print("변경후: ", data.readcnt)
    return render(request, "showContent.html", {"data":data})

def writeContent(request):
    return render(request, "writeContent.html")

def writeContentOk(request):
    if request.method == "POST":
        try:
            numcode = 1
            lists = Shopboard.objects.all()
            if lists.count() != 0:
                numcode = Shopboard.objects.latest("num").num + 1
                #print("gcode: ", gcode) 
            
        except Exception as e:
            print("writeContentOk err: ", e)
            
        Shopboard(
            num = numcode,
            name = request.POST.get("name"),
            readcnt = 0,
            bip=socket.gethostbyname(socket.getfqdn()),
            bdate=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            pass_field = request.POST.get("pass_field"),
            title = request.POST.get("title"),
            cont = request.POST.get("cont"),
        ).save()
    return HttpResponseRedirect("/myboard/boardList/")

def modifyContent(request):
    try:
        data = Shopboard.objects.get(num=request.GET.get("num"))
    except Exception as e:
        print("modifyContent err: ", e)
    return render(request, "modifyContent.html", {"data":data})

def modifyContentOk(request):
    if request.method == "POST":
        try:
            modifyData = Shopboard.objects.get(num=request.POST.get("num"))
            modifyData.name = request.POST.get("name")
            modifyData.title = request.POST.get("title")
            modifyData.cont = request.POST.get("cont")
            modifyData.save()
        except Exception as e:
            print("modifyContentOk err: ", e)
        
    return HttpResponseRedirect("/myboard/boardList/")

def deleteContent(request):
    delData = Shopboard.objects.get(num=request.GET.get("num"))
    delData.delete()
    return HttpResponseRedirect("/myboard/boardList/")

