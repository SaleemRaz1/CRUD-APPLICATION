from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User    
# Create your views here.

def Add_Show(request):
 if request.method == 'POST':
    fm=StudentRegistration(request.POST)
    if fm.is_valid():
        nm=fm.cleaned_data['name']
        eml=fm.cleaned_data['email']
        pwd=fm.cleaned_data['password']
        reg=User(name=nm,email=eml,password=pwd)
        reg.save()    
        fm=StudentRegistration()
 else:
     fm=StudentRegistration()
 stud=User.objects.all()
 return render(request,'enroll/AddandShow.html',{'form':fm,'stud':stud})

# this function is for updation 
def Update_Data(request,id):
    if request.method=='POST':
        deta=User.objects.get(pk=id) 
        fm=StudentRegistration(request.POST,instance=deta)
        if fm.is_valid():
            fm.save()
    else:
        deta=User.objects.get(pk=id) 
        fm=StudentRegistration(instance=deta)
                
    return render (request,'enroll/updateStudent.html',{'form':fm})






def Base(request):
    return render(request,'enroll/base.html')


# this function will delete the data
def Delete_Data(request,id):
 if request.method == 'POST':
    delet = User.objects.get(pk=id)
    delet.delete()
    return HttpResponseRedirect('/')
        
