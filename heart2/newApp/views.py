from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PredictForm, SignUpForm, SignInForm
from django.contrib.auth.models import User

def evaluate_conditions(input_values):
    Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, Slope = input_values

    risk_factors = 0

    FastingBS = int(FastingBS)
    ExerciseAngina = int(ExerciseAngina)
    Slope = int(Slope)

    if Age > 50:
        risk_factors += 1
    if Sex == 1:
        risk_factors += 1
    if ChestPainType == 1 or ChestPainType == 3:
        risk_factors += 1
    if RestingBP > 140:
        risk_factors += 1
    if Cholesterol > 240:
        risk_factors += 1
    if FastingBS == 1:
        risk_factors += 1
    if RestingECG == 1 or RestingECG == 2:
        risk_factors += 1
    if MaxHR < 140:
        risk_factors += 1
    if ExerciseAngina == 1:
        risk_factors += 1
    if Oldpeak > 1.0:
        risk_factors += 1
    if Slope == 2:
        risk_factors += 1

    if risk_factors >= 5:
        return "You May Have Heart Failure"
    else:
        return "No Heart Failure Detected"

def home(request):
    return render(request, 'newApp/home.html')

def base(request):
    return render(request,'newApp/base.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'You have successfully signed up! Please sign in to continue.')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'newApp/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = SignInForm()
    return render(request, 'newApp/signin.html', {'form': form})

@login_required
def predict(request):
    form = PredictForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Age = form.cleaned_data['age']
        Sex = form.cleaned_data['sex']
        ChestPainType = form.cleaned_data['chest_pain_type']
        RestingBP = form.cleaned_data['resting_bp']
        Cholesterol = form.cleaned_data['cholesterol']
        FastingBS = form.cleaned_data['fasting_bs']
        RestingECG = form.cleaned_data['resting_ecg']
        MaxHR = form.cleaned_data['max_hr']
        ExerciseAngina = form.cleaned_data['exercise_angina']
        Oldpeak = form.cleaned_data['oldpeak']
        Slope = form.cleaned_data['slope']

        input_values = [Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, Slope]

        result = evaluate_conditions(input_values)

        return redirect('result', result=result)
    return render(request, 'newApp/predict.html', {'form': form})

@login_required
def result(request, result):
    return render(request, 'newApp/result.html', {'result': result})

def about(request):
    return render(request, 'newApp/about.html')
