from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from django.http import HttpResponse
from django.contrib import messages

from forum.settings import BASE_DIR, MEDIA_URL
# Create your views here
from .models import Theme, Question, Answer
from django.db.models import Q


def index(request):
    theme = Theme.objects.all()
    questions = Question.objects.all()
    # a = questions.answers_set.all()
    # questions = Question.objects.filter(theme__isnull=False)
    print(  MEDIA_URL )
    content = {'themes': theme, 'questions': questions}
    return render(request, 'app/index.html', content)


def questionIndex(request, pk):
    # room = Answer.objects.get(id=pk)

    question = Question.objects.get(id=pk)
    print(question)
    
    content = { 'question': question}
    return render(request, 'app/question.html', content)

    