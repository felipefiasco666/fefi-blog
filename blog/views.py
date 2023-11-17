
from django.shortcuts import get_object_or_404, render,redirect
from .forms import TopicForm,EntryForm
from .models import Topic,Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404
def index(request):
    return render(request,'blog/index.html')
@login_required
def topics(request):
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'blog/topics.html',context)
@login_required
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'blog/topic.html',context)
@login_required
def new_topic(request):
    if request.method!='POST':
        form=TopicForm()
    else:
        form=TopicForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return redirect('blog:topics') 
    context={'form':form}
    return render(request,'blog/new_topic.html',context) 
@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('blog:topic',topic_id=topic_id)
    context={'topic':topic,'form':form}
    return render(request,'blog/new_entry.html',context) 
@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id) 
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method!='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:topic',topic_id=topic.id)
    context={'entry':entry,'form':form,'topic':topic}
    return render(request,'blog/edit_entry.html',context)  
@login_required
def delete(request,topic_id):
        topic=Topic.objects.get(id=topic_id)
        if topic.owner!=request.user:
            raise Http404
        context={'topic':topic}
        if request.method=='GET':
            return render(request,'blog/delete.html',context)
        elif request.method=='POST':
            topic.delete()
            return redirect('blog:topics')
       
    



# Create your views here.
