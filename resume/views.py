from django.shortcuts import render
from resume.models import OnlyImage
# Create your views here.

def home(request):
    template_name = 'land.html'
    image = OnlyImage.objects.all()
    return render(request,template_name,{'Image':image})
def resume(request):
    template_name = 'home.html'
    return render(request,template_name)