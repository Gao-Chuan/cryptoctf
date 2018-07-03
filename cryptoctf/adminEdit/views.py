from django.shortcuts import render, redirect, reverse  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from .forms import UploadFileForm
from . import models


def handle_upload_file(name, file):
    with open("./media/%s" % name + file.name, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)

def download(request, id):
    def file_iterator(file, chunk_size=512):
        with open(file) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    
    challenge = models.challengeinfo.objects.get(id = id)
    attachment = challenge.attachment
    filename = './media/'+attachment
    response = StreamingHttpResponse(file_iterator(filename))

    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    
    return response


# Create your views here.
def do_login(request, ):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']

        user = authenticate(request, username='admin', password=pw)
        if user != None:
            login(request, user)
            return redirect(reverse('edit:list'))
        else:
            return HttpResponse('hello')
        
    else:
        return render(request, 'edit/login.html', {})

@login_required(login_url = '/edit/login')
def challengeList(request):
    if request.user.username != 'admin':
        return HttpResponse('hello')
    challenges = models.challengeinfo.objects.all().values('name', 'id')
    
    try:
        id = models.challengeinfo.objects.latest('id')
        id.value()
    except:
        id = -1
    return render(request, 'edit/list.html', {'challenges':challenges, 'id':id+1})

@login_required(login_url = '/edit/login')
def add(request, ):
    if request.user.username != 'admin':
        return HttpResponse('hello')
    
    try:
        id = models.challengeinfo.objects.latest('id')
        id.value()
    except:
        id = -1
    
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'edit/add.html', {'challenge':{}, 'id':id+1, 'form':form})

    name = request.POST['name']
    description = request.POST['description']
    group = request.POST['group']
    pt = request.POST['pt']
    flag = request.POST['flag']
    author = request.POST['author']
    
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        handle_upload_file(name, request.FILES['file'])
        attachment = name + request.FILES.get("file", None).name
    else:
        attachment = None
    
    models.challengeinfo.objects.create(name = name, description = description, group = group, pt = pt, flag = flag, times = 0, attachment = attachment, author = author)    
    return redirect(reverse('edit:list'))


@login_required(login_url = '/edit/login')
def edit(request, id):
    if request.user.username != 'admin':
        return HttpResponse('hello')
    if request.method == 'GET':
        form = UploadFileForm()
        challenge = models.challengeinfo.objects.get(id = id)
        return render(request, 'edit/edit.html', {'challenge':challenge.__dict__, 'id':id, 'form':form})

    delete = request.POST['delete']
    if delete == 'yes':
        models.challengeinfo.objects.filter(id = id).delete()
        return redirect(reverse('edit:list'))
    

    name = request.POST['name']
    description = request.POST['description']
    group = request.POST['group']
    pt = request.POST['pt']
    flag = request.POST['flag']
    author = request.POST['author']
    
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        handle_upload_file(name, request.FILES['file'])
        attachment = name + request.FILES.get("file", None).name
    else:
        attachment = None

    try:    
        obj = models.challengeinfo.objects.get(id = id)
        obj.name = name
        obj.description = description
        obj.group = group
        obj.pt = pt
        obj.flag = flag
        obj.author = author
        obj.attachment = attachment
        obj.save()
    except:
        HttpResponse('wrong id')

    return redirect(reverse('edit:list'))
