from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NewUserForm,Valueform
from  django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test,login_required



def Sign_up_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(User.objects.all())
            messages.success(request, "Registration successful." )
            return redirect("http://127.0.0.1:8000/")
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request,template_name="Signup.html", context={"Sign_up_form":form})

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            print('1',request.user.is_authenticated, request.user)
            login(request, user)
#            logout(request)
            print('1',request.user.is_authenticated, request.user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("http://127.0.0.1:8000/")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
   if request.user.is_authenticated:
        logout(request)
        print('2',request.user.is_authenticated, request.user)
        messages.info(request, "Logged out successfully!")
        return redirect("http://127.0.0.1:8000/")

def Welcome_page(request):
    return  render(request,'Welcomepage.html')

@login_required
def form_view(request):
    form = Valueform(request.POST or None,files=request.FILES)
    if form.is_valid():
        post = form.save()
        post.Creator = request.user
        print('Creator user stored',request.user)
        post.save()
    return  render(request,'form.html', {"form": form})

@login_required
def profile_page(request,pk):
      context2 = {}
      Key_details = Bride.objects.get(id=pk)
      Profile_name =  Key_details.name
      Profile_Age =  Key_details.age
      Profile_Thegai =  Key_details.thegai
      Profile_state =  Key_details.State
      Profile_district =  Key_details.District
      Profile_Address =  Key_details.Address
      Profile_Phone =  Key_details.Phone
      Profile_Profession =  Key_details.profession
      Profile_Salary =  Key_details.salary
      Profile_UG =  Key_details.Under_Graduation_Degree
      Profile_UGC =  Key_details.Under_Graduation_college
      Profile_PG =  Key_details.Post_Graduation_Degree
      Profile_PGC =  Key_details.Post_Graduation_college
      Profile_Rasi =  Key_details.Rasi
      Profile_Nakshatra =  Key_details.Nakshatra
      Profile_Image =  Key_details.Image
      context2['Age'] = Profile_Age
      context2['name'] = Profile_name
      context2['thegai'] = Profile_Thegai
      context2['State'] = Profile_state
      context2['district'] = Profile_district
      context2['Address'] = Profile_Address
      context2['Phone'] = Profile_Phone
      context2['profession'] = Profile_Profession
      context2['Under_Graduation_Degree'] = Profile_UG
      context2['Under_Graduation_college'] = Profile_UGC
      context2['Post_Graduation_Degree'] = Profile_PG
      context2['Post_Graduation_college'] = Profile_PGC
      context2['Rasi'] = Profile_Rasi
      context2['Nakshatra'] = Profile_Nakshatra
      context2['Image'] = Profile_Image
      print(Key_details.Creator)
      print(context2)
      return  render(request,'Profilepage.html',context2)
#    return  render(request,'Profilepage.html',{"form": form})

def Main_page(request):
    Post_keys = []
    bride_id_str_list = []
    brides = Bride.objects.all()
#    Bride_Image = brides.Image
#    context2['Image'] = Bride_Image
    context = {'brides':brides}
    if request.method == 'GET':
            State = request.GET.get('state', '')
            District = request.GET.get('district', '')
            thegai = request.GET.get('thegai', '')
            Rasi = request.GET.get('Rasi', '')
            print(len(State),len(District),District, Rasi)
            if len(State) > 0:
                Filter_context = {}
                bride = Bride.objects.filter(State=str(State))
                Filter_context = {'brides':bride}
                return  render(request,'Mainpage.html',Filter_context)
            if len(District) > 0:
                Filter_context = {}
                bride = Bride.objects.filter(District=str(District))
                print(bride)
                Filter_context = {'brides':bride}
                return  render(request,'Mainpage.html',Filter_context)
            if len(thegai) > 0:
                Filter_context = {}
                bride = Bride.objects.filter(thegai=str(thegai))
                print(bride)
                Filter_context = {'brides':bride}
                return  render(request,'Mainpage.html',Filter_context)
            if len(Rasi) > 0:
                Filter_context = {}
                bride = Bride.objects.filter(Rasi=str(Rasi))
                print(bride)
                Filter_context = {'brides':bride}
                return  render(request,'Mainpage.html',Filter_context)

    return  render(request,'Mainpage.html',context)

@login_required
def profile_reg_user(request):
    Filter_context = {}
    current_user = request.user
    bride = Bride.objects.filter(Creator=current_user)
    Filter_context = {'brides':bride}
    return  render(request,'Profiles_reg_user.html',Filter_context)

@login_required
def form_update(request,pk):
    update_profile = Bride.objects.get(id=pk)
    form = Valueform(instance=update_profile)
    context = {'form':form}
    if request.method == 'POST':
        form = Valueform(request.POST,instance=update_profile,files=request.FILES)
        print(form)
        if form.is_valid():
            post = form.save()
            post.Creator = request.user
            print('Creator user stored',request.user)
            post.save()
            obj = form.instance
            return  render(request,'form.html', {"obj": obj,"form": form})
    return  render(request,'form.html', {"form": form})
