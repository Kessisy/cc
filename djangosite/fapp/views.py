from django.shortcuts import render
from django.http import HttpResponse
#from fapp.forms import MomentForm
from django.http import HttpResponseRedirect
from django.template import loader,RequestContext
import os
from django.urls import reverse
from django.contrib import auth
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt 
def signup(request):
    def __is_login(request):
        return request.session.get('islogin',False)
    def _do_signup(request,_userinfo):
        _state={
            'success':True,
            'message':'welcome to my site',
        }
        if(_userinfo['username']==''):
            _state['success']='False'
            _state['message']='please input your username'
            return _state
        if _userinfo['password']=='':
            _state['success']='False'
            _state['message']='please input your password'
            return _state
        if _userinfo['email']=='':
            _state['success']='False'
            _state['message']='please input your email'
            return _state
        
        if _userinfo['password']!=_userinfo['comfirm']:
            
            _state['success']='False'
            _state['message']='please input your password again'
            return _state  
        _user=models.User(
        username=_userinfo['username'],
        password=_userinfo['password'],
        email=_userinfo['email'],
        #area=models.Area.objects.get(id=1),
        )
    #models.User.save()
        return _state
    _islogin=__is_login(request)
    if(_islogin):
        return HttpResponseRedirect('/signup/')
    _userinfo={
        'username':'',
        'password':'',
        'comfirm':'',
        'email':'',
        }
    try:
        _userinfo={
        'username':request.POST.get('username'),
        'password':request.POST.get('password'),
        'comfirm':request.POST.get('comfirm'),
        'email':request.POST.get('email'),
        }
        _is_post=True
    except(KeyError):
        _is_post=False
        
    if(_is_post):
        _state=_do_signup(request,_userinfo)
    else:
        _state={
            'success':False,
            'message':'please sign up first'}
    '''if(_state['success']):
        _state['message']='signed up success'
    '''
    _result={
        'success':_state['success'],
        'message':_state['message'],
        'form':{
            'username':_userinfo['username'],
            'password':_userinfo['password'],
            'comfirm':_userinfo['comfirm'],
            'email':_userinfo['email'],
            }
        }
    _template=loader.get_template('signup.html')
    _context={
       'page_title':'Sign up',
       'state':_result,
    }
    _output=_template.render(_context)
    return HttpResponse(_output)


    
        
     



    
        