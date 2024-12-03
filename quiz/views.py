from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Question, Submission, USER_MODEL
# Create your views here.


def login_view(request: HttpRequest):
    context = {'error': False}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context['error'] = True
            context['message'] = "Unable to Login with Given Credentials"
    return render(request, 'login.html', context=context)


@login_required
def logout_view(request: HttpRequest):
    logout(request)
    return redirect(to='login')


def register_view(request: HttpRequest):
    context = {'error': False}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = USER_MODEL.objects.create_user(
                username=username, password=password, email=email)
            login(request, user)
            return redirect(to='dashboard')
        except Exception as e:
            context['error'] = True
            context['message'] = e
    return render(request, 'register.html', context=context)


@login_required
def dashboard_view(request: HttpRequest):
    submissions = Submission.objects.filter(user=request.user)
    total = submissions.count()
    correct = submissions.filter(is_correct=True).count()
    overall = 0 if total == 0 else correct/total*100
    return render(request, 'dashboard.html', context={'total': total, 'correct': correct, 'overall': overall})


@login_required
def question_view(request: HttpRequest):
    context = {}
    if request.method == 'GET':

        user = request.user
        questions_set = Question.objects.exclude(submissions__user=user)

        question = questions_set.first()
        context['question'] = question
        request.session['current_question'] = question.id if question else None
    else:
        answer = int(request.POST.get('answer'))
        question = Question.objects.get(pk=request.session.get(
            'current_question')) if request.session.get('current_question') else None
        # submissionx
        submission_obj = Submission.objects.filter(
            user=request.user, question=question).first()
        if submission_obj == None:
            submission_obj = Submission.objects.create(
                user=request.user, question=question, is_correct=answer == question.correct_option)
        context['question'] = question
        context['is_answered'] = True
        context['is_correct'] = submission_obj.is_correct
        context['option1'] = answer == 1
        context['option2'] = answer == 2
        context['option3'] = answer == 3
        context['option4'] = answer == 4

    return render(request, 'question.html', context=context)
