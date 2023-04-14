import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            result = round(a + b, 2)
            answer['answer'] = result
        except ValueError:
            answer['error'] = 'Enter only numbers please'
            return JsonResponse(answer, status=400)
        return JsonResponse(answer)


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            result = round(a - b, 2)
        except ValueError:
            answer['error'] = 'Enter only numbers please'
            return JsonResponse(answer, status=400)
        answer['answer'] = result
        return JsonResponse(answer)


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            result = round(a * b, 2)
        except ValueError:
            answer['error'] = 'Enter only numbers please'
            return JsonResponse(answer, status=400)
        answer['answer'] = result
        return JsonResponse(answer)


@csrf_exempt
def divide_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            result = round(a / b, 2)
            answer['answer'] = result
            return JsonResponse(answer)
        except ZeroDivisionError:
            answer['error'] = "Division by zero!"
            return JsonResponse(answer, status=400)
        except ValueError:
            answer['error'] = 'Enter only numbers please'
            return JsonResponse(answer, status=400)
