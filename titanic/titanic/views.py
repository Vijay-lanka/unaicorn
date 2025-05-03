from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    Pclass = int(request.GET["pclass"])
    Age = int(request.GET["age"])
    SibSp = int(request.GET["Sibsp"])
    parch = int(request.GET["parch"])
    Fare = int(request.GET["fare"])
    predict = ml_predict.pred_model(Pclass,Age,SibSp,parch,Fare)
    return render(request, 'result.html', {'prediction': predict})
