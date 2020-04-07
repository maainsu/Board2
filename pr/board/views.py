from django.shortcuts import render

from django.shortcuts import render
from board.models import board, Comment
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def list(request):
    boardCount = board.objects.count()
    boardList = board.objects.all().order_by("-idx")
    return render(request, "list.html", {"boardList" : boardList, "boardCount" : boardCount})   
def write(request):
    return render(request, "write.html")
@csrf_exempt
def insert(request):
    fname = ""
    fsize = 0
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file.name
        fsize = file.size
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        
    dto = Board(writer = request.POST["writer"], title = request.POST["title"], content = request.POST["content"], filename = fname, filesize = fsize)
    dto.save()
    print(dto)
    return redirect("/")