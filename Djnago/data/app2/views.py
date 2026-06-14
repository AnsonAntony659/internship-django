from django.shortcuts import render
from . forms import RegisterForms
# Create your views here.
 
def home(request):
  return render(request,'home.html')



def Register_Form(request):
  if request.method=='POST':
    form=RegisterForms(request.POST)

    if form.is_valid():
      name=form.cleaned_data['name']
      address=form.cleaned_data['address']
      pincode=form.cleaned_data['pincode']

      print(name,address,pincode)
 
  else:
    form=RegisterForms()

  return render(request,'RegisterForm.html',{'form':form})

