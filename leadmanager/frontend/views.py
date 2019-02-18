from django.shortcuts import render


def index(reqest):
    return render(reqest, 'frontend/index.html')