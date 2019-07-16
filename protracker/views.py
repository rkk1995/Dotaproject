from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def index(request):
    return render(request, 'protracker.jinja')
