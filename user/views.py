from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.template import Context, loader
from django.http import HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required

from user.users import users

def loginView(request):
    if 'username' in request.POST:
        data = request.POST
        u = users()
        
        user = u.checkCredentials(data['username'], data['password'])
        if user:
            # the password verified for the user
            if "inactive" in user and user['inactive'] == "1":
                context = RequestContext(request, {"message" : "Account is inactive."})
                return render_to_response('login.html',context,context_instance=RequestContext(request))
            else:
                request.session['userId'] = user["_id"]
                return HttpResponseRedirect("/")
        else:
            # the authentication system was unable to verify the username and password
            context = RequestContext(request, {"message" : user})
            return render_to_response('login.html',context,context_instance=RequestContext(request))
    else:
        context = RequestContext(request, {})
        return render_to_response('login.html',context,context_instance=RequestContext(request))
    
def createUserView(request):
    if 'username' in request.POST:
        data = request.POST
        u = users()
        
        if not u.userExists(data['username']):
            u.lastName = data['lastName']
            u.firstName = data['firstName']
            u.email = data['email']
            u.userName = data['username']
            u.password = data['password']
            u.admin = "1"
            
            request.session['userId'] = u.save()
            return HttpResponseRedirect("/")
        else:
            context = RequestContext(request, {"message" : "Username already being used"})
            return render_to_response('signup.html',context,context_instance=RequestContext(request))
    else:
        context = RequestContext(request, {})
        return render_to_response('signup.html',context,context_instance=RequestContext(request))

def logoutView(request):
    del request.session['userId']
    return HttpResponseRedirect("/")