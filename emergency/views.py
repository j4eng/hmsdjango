from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
from .models import emergency
from .forms import MyForm
# Create your views here.


def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'emergency.html', {'form': form})