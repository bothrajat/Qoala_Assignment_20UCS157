from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.db import transaction
from models import *
import json, ast

def home(request):
    return redirect("add")
def add(request):
    return render(request,"add.html")
def update(request):
    return render(request,"update.html")
def display(request):
    return render(request,"display.html")
def delete(request):
    return render(request,"delete.html")
