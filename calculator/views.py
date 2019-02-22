from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def calculator(request):
    head = 'This is your calculator app.<br/>'
    a = 'Adding 20 + 10 = 30 : /add/20/10/<br/>'
    b = 'Subtracting 20 - 10 = 10 : /subtract/20/10<br/>'
    c = 'Multiply 20 * 10 = 200 : /multiply/20/10<br/>'
    d = 'Divide 20 / 10 = 2 : /divide/20/10'
    text = head + a + b + c + d

    return HttpResponse(text, status=200)


def add(request, a, b):
    c = a + b
    return_str = 'The sum is: ' + str(c)

    return HttpResponse(return_str)


def subtract(request, a, b):
    c = a - b
    return_str = 'The difference is: ' + str(c)

    return HttpResponse(return_str)


def multiply(request, a, b):
    c = a * b
    return_str = 'The product is: ' + str(c)

    return HttpResponse(return_str)


def divide(request, a, b):
    c = a / b
    return_str = 'The quotient is: ' + str(c)

    return HttpResponse(return_str)
