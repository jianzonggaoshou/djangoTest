import logging
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response


def login_view(request):
    pass
    temp = request.path
    logging.warning(temp)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logging.warning(username)
        logging.warning(password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            logging.warning('aaaaaaaaaaa')
            # flag = False
            # if flag:
            #     settings.LOGIN_REDIRECT_URL = '/index/'
            #     return redirect(settings.LOGIN_REDIRECT_URL)
            # else:
            #     settings.LOGIN_REDIRECT_URL = '/admin/'
            #     return redirect(settings.LOGIN_REDIRECT_URL)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "login_test/login.html")


class GetStaticUrl(APIView):

    def post(self, request):
        temp = request.data
        temp = temp['cilentUser']
        logging.warning(temp)
        if '/env/' in temp:
            settings.LOGIN_REDIRECT_URL = '/env/'
            logging.warning(settings.LOGIN_REDIRECT_URL)
            return Response(settings.LOGIN_REDIRECT_URL, 200)
            # settings.LOGIN_REDIRECT_URL = '/service/'
        elif '/service/' in temp:
            settings.LOGIN_REDIRECT_URL = '/service/'
            logging.warning(settings.LOGIN_REDIRECT_URL)
            return Response(settings.LOGIN_REDIRECT_URL, 200)
        else:
            settings.LOGIN_REDIRECT_URL = '/service/'
            logging.warning(settings.LOGIN_REDIRECT_URL)
            return Response(settings.LOGIN_REDIRECT_URL, 200)


