from django.shortcuts import render
from .forms import ImgForm
from .models import Image
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()        
    form = ImgForm()
    img = Image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})


def index(request):
    return render(request,'index.html')