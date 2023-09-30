from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello, world!')


def hello_re(request, s):
    return HttpResponse(f'Hello, {s} world!')


def hello_encode(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')
