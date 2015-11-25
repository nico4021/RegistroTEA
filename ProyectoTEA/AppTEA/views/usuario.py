# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Sistema de logueo de usuarios.
"""
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
                context = {
                    'bad_login': "Su cuenta esta inactiva"
                }
                return render_to_response('bad_login.html', context)
        else:
            # Bad login details were provided. So we can't log the user in.
            
            context = {
                    'bad_login': "Usuario o contraseña invalidos"
                }
            return render_to_response('bad_login.html', context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:

	# No context variables to pass to the template system, hence the
	# blank dictionary object...
	
	return render_to_response('login.html', context)

"""
Sistema de deslogueo de usuarios.
"""
def desloguearse(request):
    logout(request)

    return redirect('/')