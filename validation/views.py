from django.shortcuts import render
from .forms import  TweakModelForm,CrispyModelForm,DefaultModelForm
from .models import CrispyModel, TweakModel, DefaultModel

# Create your views here.
def home(request):   
    return render(request, 'validation/home.html')

def CrispyFormHome(request):
    if request.method=='POST':
        form = CrispyModelForm(request.POST)
        if form.is_valid():
            print('Validation')
            print('First Name:', form.cleaned_data['firstname'])
            print('First Last:', form.cleaned_data['lastname'])
            print('Email:', form.cleaned_data['email'])
            print('Phone', form.cleaned_data['phone'])
            print('Password', form.cleaned_data['password'])
    else:
        form = CrispyModelForm()
    return render(request, 'validation/crispyform_home.html',{'form':form})

def TweakFormHome(request):
    if request.method=='POST':
        form = TweakModelForm(request.POST)
        if form.is_valid():
             print('Validation')
    else:
        form = TweakModelForm()
    return render(request, 'validation/tweakform_home.html',{'form':form})

def DefaultFormHome(request):
    if request.method=='POST':
        form = DefaultModelForm(request.POST)
        if form.is_valid():
            print('Validation')
            print('First Name:', form.cleaned_data['firstname'])
            print('First Last:', form.cleaned_data['lastname'])
            print('Email:', form.cleaned_data['email'])
            print('Phone', form.cleaned_data['phone'])
            print('Password', form.cleaned_data['password'])
    else:
        form = DefaultModelForm()
    return render(request, 'validation/defaultform_home.html',{'form':form})

