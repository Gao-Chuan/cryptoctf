from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponse
from adminEdit import models
from account import models as am
import json

# Create your views here.
def check(request, id):
    # flag in the post method
    challenge = models.challengeinfo.objects.get(id = int(id))
    # 检查flag是否正确
    try:
        assert request.POST['flag'] == challenge.__dict__['flag']
    except:
        return HttpResponse('wrong')
    
    # 加分，加id进doneList
    username = request.user.username
    user = am.userinfo.objects.get(username = request.user.username)
    dl = json.loads(user.__dict__['doneList'])['doneList']
    if id in dl:
        return HttpResponse('You have solve this game, please donot submit twice.')
    else:
        dl.append(id)
        obj = am.userinfo.objects.get(username = request.user.username)
        obj.doneList = json.dumps({"doneList": dl})
        obj.pt = obj.pt + challenge.__dict__['pt']
        obj.save()
    
    # 加first30solvers
    solvers = json.loads(challenge.__dict__['solvers'])['solvers']
    if len(solvers) <= 30:
        solvers.append(request.user.username)
        challenge.times = challenge.times + 1
        challenge.solvers = json.dumps({"solvers": solvers})
        challenge.save()
    
    return render(request, 'submit/succeed.html', {})