from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, PostCategory, Like
from django.http import HttpResponse
from django.contrib import messages
from .forms import PostForm

# Create your views here.
@login_required
def create_post(request):
    if request.user.is_authenticated:
        form = PostForm()
        category = PostCategory.objects.all()
        context = {
            'form': form,
            'category' : category
        }
        if request.method == 'POST':
            form = PostForm(request.POST,  request.FILES)
            context = {
            'form': form,
            'category' : category
            }
            print(request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                form.save()
                messages.success(request, 'Post Add successfully!')
                return redirect('post_list')
            else:
                return render(request, 'post/add.html', context)
        return render(request, 'post/add.html', context)
    else:
         return redirect('login')

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        context = {
            'posts' : posts
        }
        return render(request, 'post/list.html', context)
    else:
         return redirect('login')


def post_view(request, pk=None, *args, **kwargs):
    if request.user.is_authenticated:
        instance = get_object_or_404(Post, pk=pk)
        print(instance)
        context ={
            'object' : instance
        }
        return render(request, 'post/view.html', context)
    else:
         return redirect('login')

def post_edit(request, pk=None, *args, **kwargs):
    category = PostCategory.objects.all()
    if request.user.is_authenticated:
        obj = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST or None, request.FILES or None,  instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Update successfully!')
            return redirect('post_list')

        context ={
            'form' : form,
            'category' : category
        }
        return render(request, 'post/edit.html', context)
    else:
         return redirect('login')    

def post_delete(request, pk=None, *args, **kwargs):
    if request.user.is_authenticated:
        obj = get_object_or_404(Post, pk=pk)
        obj.delete()
        messages.success(request, 'Post Delete successfully!')
        return redirect('post_list')
    else:
         return redirect('login')    

def post_like(request):
    # obj = get_object_or_404(Post, pk=pk)
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = get_object_or_404(Post, pk=pk)
        print(obj)
        user = request.user
        print(user)
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
                result = False
            else:
                obj.likes.add(user)
                result = True

    else:
        result = False
    return HttpResponse(result)

   