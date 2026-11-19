"""Views for the madad project."""

from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html


def home(request):
    return HttpResponse(format_html(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Madad</title></head><body><main><h1>Madad</h1>'
        '<p><a href="{}">Administration</a></p></main></body></html>',
        reverse('admin:index'),
    ))
