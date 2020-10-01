from django.shortcuts import render
from django import forms
from demoapp.forms import UserprofileInfoFrom, UserForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):

    return render(request, 'demoapp/index.html')

@login_required
def special(request):
    return HttpResponse("your logged in , nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def form_name_views(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("SUCCESSFUL!!")
            print('name of new user:' + form.cleaned_data['name'])
            print('Email of new user' + form.cleaned_data['email'])
            print('Text of confidence:' + form.cleaned_data['text'])
            print('SIGNED UP WITH THIS DETAILS')


    # Create your views here.
    return render(request, 'demoapp/formpage.html', {'form': form})
def basic(request):
    return render(request, 'demoapp/basic.html')
def others(request):
    context_dict = {'text': "hello world", 'number': 1000}
    return render(request, 'demoapp/others.html', context_dict)
def relative(request):
    return render(request, 'demoapp/template.html')



    pass


def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserprofileInfoFrom(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserprofileInfoFrom()

    return render(request, 'demoapp/registration.html',
                  {'user_form':user_form,
                  'profile_form':profile_form,
                   'registered': registered})



    return render(request, 'demoapp/registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("someone tried to login and failed!!")
            print("Username: {} and password: {} ".format(username,password))
            return  HttpResponse("INVALID LOGIN DETAILS")
    else:
        return render(request, 'demoapp/login.html', {})


