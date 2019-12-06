from django.shortcuts import render,redirect
from .models import data

from .forms import dataForm

# Create your views here.
def index(request):
	form = data.objects.all()
	return render(request,'home.html',{'form':form})


def add_post(request):
	if request.method == 'POST':
		form = dataForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = dataForm()
		return render(request,'add_post.html',{'form':form})
