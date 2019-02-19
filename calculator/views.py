from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def calculator(request):
    text = 'This is your calculator app.'

    return HttpResponse(text, status=200)


def add(request, a, b):
    sum = a + b
    return_str = 'The sum is: ' + str(sum)

    return HttpResponse(return_str)


def subtract(request, a, b):
    difference = a - b
    return_str = 'The difference is: ' + str(difference)

    return HttpResponse(return_str)


def multiply(request, a, b):
    product = a * b
    return_str = 'The product is: ' + str(product)

    return HttpResponse(return_str)


def divide(request, a, b):
    quotient = a / b
    return_str = 'The quotient is: ' + str(quotient)

    return HttpResponse(return_str)