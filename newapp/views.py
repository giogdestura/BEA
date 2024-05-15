from django.shortcuts import redirect, render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def memberlist(request):
    mem=Member.objects.all()
    return render(request,'memberlist.html',{'mem':mem})

def records(request):
    mem=Member.objects.all()
    return render(request,'records.html',{'mem':mem})

def dashboard2(request):
    mem=Member.objects.all()
    return render(request,'dashboard2.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("memberlist")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("memberlist")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("memberlist")

def increment_click(request, id):
    mem = Member.objects.get(id=id)
    mem.click_count += 1
    mem.save()
    return redirect('testing')

def present(request, id):
    mem = Member.objects.get(id=id)
    mem.present_count += 1
    mem.save()
    return redirect('testing')

def absent(request, id):
    mem = Member.objects.get(id=id)
    mem.absent_count += 1
    mem.save()
    return redirect('testing')

def late(request, id):
    mem = Member.objects.get(id=id)
    mem.late_count += 1
    mem.save()
    return redirect('testing')

def testing(request):
    mem=Member.objects.all()
    return render(request,'testing.html',{'mem':mem})
