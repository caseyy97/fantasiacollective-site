from django.shortcuts import render
from .models import SiteConfig, Headmate

# Create your views here.
def index(request):
    context = {"SiteConfig": SiteConfig.objects.get(), "Headmates": Headmate.objects.all().order_by("order")}
    return render(request, "home.html", context)