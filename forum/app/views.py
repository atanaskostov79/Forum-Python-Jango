from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
# Create your views here
from .models import Theme, Question, Answer, User
from django.db.models import Q
from .forms import MyUserCreationForm, UserForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'app/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'app/register.html',{'form': form})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'app/update-user.html', {'form': form})



def index(request):
    theme = Theme.objects.all()
    questions = Question.objects.all()
    content = {'themes': theme, 'questions': questions}
    print(questions)
    return render(request, 'app/index.html', content)
    
def questionLike(request, pk):
    question = Question.objects.get(id=pk)
    question.like.add(request.user)
    question.save()
    return redirect('question', pk)

def questionDislike(request, pk):
    question = Question.objects.get(id=pk)
    question.dislike.add(request.user)
    question.save()
    return redirect('question', pk)

def questionIndex(request, pk):
    question = Question.objects.get(id=pk)
    # if (ak == 'like'):
    #     question.like += 1
    # elif(ak == 'dislike'):
    #     question.dislike += 1
    question.view +=1 
    question.save()
    content = { 'question': question}
    return render(request, 'app/question.html', content)

def theme(request, pk):
    theme = Theme.objects.get(id=pk)
    question = Question.objects.get(theme_id=pk)

    print(theme)
    content = { 'questions': question }
    return render(request, 'app/question.html', content)

    