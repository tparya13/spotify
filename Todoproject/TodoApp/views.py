from django.shortcuts import render,redirect
from .models import Music
from .forms import MusicForm

def Home(req):
    musics=Music.objects.all()
    return render(req,'index.html',{'musics':musics})
def Form(req):
    if req.method=="POST": 
        name=req.POST.get('name','')
        language=req.POST.get('language','')
        duration=req.POST.get('duration','')
        image=req.FILES['image']
        description=req.POST.get('description','')        
        music=Music(name=name,language=language,duration=duration,image=image,description=description)
        music.save()
        return redirect('home')
    return render(req,'form.html')



def Details(req,id):
    musics=Music.objects.get(id=id)
    return render(req,'details.html',{'music':musics})
def Update(req,id):
    musics=Music.objects.get(id=id)
    f=MusicForm(req.POST,req.FILES or None,instance=musics)
    if f.is_valid():
        f.save()
        return redirect('home')
    return render(req,'formUpdate.html',{"music":musics,'f':f})

def Delete(req,id):
    musics=Music.objects.get(id=id)
    if req.method=="POST":
        Music.objects.filter(id=id).delete()
        return redirect('home')
    return render(req,'delete.html',{"musics":musics})