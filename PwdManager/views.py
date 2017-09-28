from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from PwdManager.models import User, Account
from django.views.decorators.csrf import csrf_exempt
import json

# User signup
@csrf_exempt
def signup(request):
    context_dict = {}

    if request.method == 'POST' or request.method == 'GET':

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        else:
            username = request.GET.get('username')
            password = request.GET.get('password')

        if username and password:
            # Check whether user is exist
            try:
                user = User.objects.get(username=username)

                context_dict['success'] = 0
                context_dict['error_message'] = 'User already exists.'

            except ObjectDoesNotExist:
                # Save user to database
                user = User.objects.create(username=username)
                user.set_password(password)
                user.save()

                context_dict['success'] = 1
        else:
            context_dict['success'] = 0
            context_dict['error_message'] = 'Invalid register details.'
    else:
        context_dict['success'] = 0
        context_dict['error_message'] = 'Incorrect Register.'

    return HttpResponse(json.dumps(context_dict), content_type="application/json")

# User login
@csrf_exempt
def login(request):
    context_dict = {}

    if request.method == 'POST' or request.method == 'GET':
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        else:
            username = request.GET.get('username')
            password = request.GET.get('password')

        # Check whether user is valid
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                context_dict['success'] = 1

                # Get account list
                account_list = Account.objects.filter(user=user).order_by('-id')
                accounts = []

                for ob in account_list:
                    account_dict = {}

                    title = ob.title
                    accountusername = ob.username
                    accountpassword = ob.password

                    account_dict['title'] = title
                    account_dict['username'] = accountusername
                    account_dict['password'] = accountpassword

                    accounts.append(account_dict)

                context_dict['accounts'] = accounts

            else:
                context_dict['success'] = 0
                context_dict['error_message'] = 'Your account is disabled.'

        else:
            context_dict['success'] = 0
            context_dict['error_message'] = 'Invalid login details.'
    else:
        context_dict['success'] = 0
        context_dict['error_message'] = 'Incorrect Login.'

    return HttpResponse(json.dumps(context_dict), content_type="application/json")

# Get account list
@csrf_exempt
def accounts(request):
    context_dict = {}

    if request.method == 'GET' or request.method == 'POST':
        if request.method == 'GET':
            username = request.GET['username']
        else:
            username = request.POST['username']

        try:
            user = User.objects.get(username=username)

            # Get account list
            account_list = Account.objects.filter(user=user).order_by('-id')
            accounts = []

            for ob in account_list:
                account_dict = {}

                title = ob.title
                accountusername = ob.username
                accountpassword = ob.password

                account_dict['title'] = title
                account_dict['username'] = accountusername
                account_dict['password'] = accountpassword

                accounts.append(account_dict)

            context_dict['accounts'] = accounts

        except ObjectDoesNotExist:
            pass

    return HttpResponse(json.dumps(context_dict), content_type="application/json")

# Upadates account list
@csrf_exempt
def updateaccounts(request):
    context_dict = {}

    if request.method == 'POST' or request.method == 'GET':
        if request.method == 'POST':
            username = request.POST.get('username')
            accounts = request.POST.get('accounts')
        else:
            username = request.GET.get('username')
            accounts = request.GET.get('accounts')

        print accounts

        accounts = json.loads(accounts)
        #accounts = json.loads('[{"username": "xingping123", "password": "zxcvv666", "title": "Twitter"}]')

        if username and accounts:

            try:
                user = User.objects.get(username=username)

                # Delete previous account list
                Account.objects.filter(user=user).delete()

                try:
                    for ob in accounts:
                        title = ob['title']
                        username = ob['username']
                        password = ob['password']

                        account = Account.objects.create(user=user, title=title, username=username, password=password)
                        account.save()

                    context_dict['success'] = 1
                except:
                    context_dict['success'] = 0
                    context_dict['error_message'] = 'Incorrect data.'

            except ObjectDoesNotExist:
                context_dict['success'] = 0
                context_dict['error_message'] = 'User not exists.'
        else:
            context_dict['success'] = 0
            context_dict['error_message'] = 'Incorrect data.'
    else:
        context_dict['success'] = 0
        context_dict['error_message'] = 'Incorrect data.'

    return HttpResponse(json.dumps(context_dict), content_type="application/json")