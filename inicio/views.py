# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
	return HttpResponse("Esta seria la pagina de inicio")
