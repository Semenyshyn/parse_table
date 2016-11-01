# coding: utf8
from django.shortcuts import render_to_response
from .models import Parts


def parse_url(request):
    return render_to_response('output.html', {'parts': Parts.objects.all()})
