
from django.shortcuts import render,redirect
from matplotlib.style import context

from .models import Post
# from django.views.generic import ListView,DetailView
# Create your views here.
def project(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'webapp/project.html',context)



def about(request, pk):
    projectObj = Post.objects.get(id=pk)
    context = {'project':projectObj}
    return render(request,'webapp/about.html',context)


from .forms import PostForm

def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'webapp/createPost.html',context)

def updatePost(request, pk):
    # fetch data from project
    project = Post.objects.get(id=pk)

    # pass data into the form using intance
    form = PostForm(instance=project)
    if request.method == "POST":
        form = PostForm()
        form = PostForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'webapp/createPost.html', context)


def deletePost(request, pk):
    project = Post.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')

    context = {'project': project}
    return render(request, 'webapp/delete.html', context)
