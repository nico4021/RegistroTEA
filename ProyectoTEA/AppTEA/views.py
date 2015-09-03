from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url="/loguearse")
def home(request):
    return HttpResponse("<h1>HOLA!!!</h1>")

def loguearse(request):
    context = RequestContext(request)
	
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
	# Usuario y contrasena
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user:
	    # Is the account active? It could have been disabled.
	    if user.is_active:
		# If the account is valid and active, we can log the user in.
		# We'll send the user back to the homepage.
		login(request, user)

		return redirect('/')

	    else:
		# An inactive account was used - no logging in!
		return HttpResponse("ERROR: cuenta inactiva.")
	else:
	    # Bad login details were provided. So we can't log the user in.
	    print "Invalid login details: {0}, {1}".format(username, password)
	    return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
	# No context variables to pass to the template system, hence the
	# blank dictionary object...
	
	return render_to_response('login.html', context)

def desloguearse(request):
    logout(request)
    
    return redirect('/loguearse')

