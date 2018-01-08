# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

import bcrypt

# Create your views here.

def index(request):
    return render(request, "map/index.html")