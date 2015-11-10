from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
import django.contrib.auth.hashers
from xhtml2pdf import pisa
from django.template.loader import get_template
from cgi import escape
import cStringIO as StringIO


from AppTEA.models import *