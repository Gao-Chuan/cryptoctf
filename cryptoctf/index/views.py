from django.shortcuts import render
from adminEdit import models
from account import models as am
import json

# Create your views here.
def index(request, ):
    try:
        tmp = models.challengeinfo.objects.filter(group = 'krill')
    except:
        tmp = []
    krill = []
    for k in tmp:
        krill.append(k.__dict__)

    try:
        tmp_s = models.challengeinfo.objects.filter(group = 'sardine')
    except:
        tmp_s = []
    sardine = []
    for s in tmp_s:
        sardine.append(s.__dict__)

    try:
        tmpt = models.challengeinfo.objects.filter(group = 'tuna')
    except:
        tmpt = []
    tuna = []
    for t in tmpt:
        tuna.append(t.__dict__)
    
    try:
        tmps =  models.challengeinfo.objects.filter(group = 'shark')
    except:
        tmps = []
    shark = []
    for s in tmps:
        shark.append(s.__dict__)
    
    try:
        tmpw = models.challengeinfo.objects.filter(group = 'whale')
    except:
        tmpw = []
    whale = []
    for w in tmpw:
        whale.append(w.__dict__)

    pt = am.userinfo.objects.filter(username = request.user.username)
    point = 0
    for e in pt:
        point = e.pt
    return render(request, 'index.html', {'krill':krill, 'sardine':sardine, 'tuna':tuna, 'shark':shark, 'whale':whale, 'pt':point})

def detail(request, id):
    challenge = models.challengeinfo.objects.get(id = int(id))
    solvers = json.loads(challenge.solvers)['solvers']
    return render(request, 'detail.html', {'challenge':challenge.__dict__, 'id':id, 'solvers':solvers})