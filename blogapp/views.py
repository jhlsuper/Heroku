from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator
from .form import BlogPost
# Create your views here.
def home(request):
    blogs = Blog.objects
    #모든 블로그 글들을 대상으로 
    blog_list =Blog.objects.all()
    #블로그 객체 세개를 한페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request 된 페이지를 얻어온뒤 return 해준다. 
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs,'post':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date= timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    #입력된 내용을 처리하는 기능 ->POST
    
    #빈페이지를 띄워주는 기능 -> Get
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():  ##입력이잘되었으면
            post = form.save(commit=False) #가지고오되 아직 저장 x
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    else:
        form = BlogPost()
        return render(request, 'new.html',{'form':form})
