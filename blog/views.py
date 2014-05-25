from django.http import HttpResponseNotFound, HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.template import Context, loader
from django.http import HttpRequest
from django.utils import timezone

from blog.posts import posts
from blog.comments import comments
from user.users import users

def page_not_found(request):
    return HttpResponseNotFound("Not FOUND MATE")

def blogs(request):
    p = posts()
    
    latestPosts = p.getLatestBlogs()
    
    template = loader.get_template('blogMain.html')
    
    user = users()
    if request.session.get('userId'):
        isSU = user.isAdmin(request.session.get('userId'))
    else:
        isSU = False
        
    context = Context({'latestPosts' : latestPosts,'isSU' : isSU})
    return HttpResponse(template.render(context))

def detail(request, blog_id):
    c = comments()
    p = posts()

    if 'n' in request.POST:
        data = request.POST
        
        c.postId = blog_id
        c.body = data['b']
        c.email = data['e']
        c.name = data['n']
        c.image = data['i']
        
        c.save()
        
    user = users()
    if request.session.get('userId'):
        isSU = user.isAdmin(request.session.get('userId'))
    else:
        isSU = False
    
    post = p.getPost(blog_id)
    comment = c.getCommentsForPost(blog_id)
    context = RequestContext(request, {'post' : post,'comments' : comment,'isSU' : isSU,'commentCount' : comment.count()})
    return render_to_response('detail.html',context,context_instance=RequestContext(request))

def new(request):
    user = users()
    if request.session.get('userId'):
        if 'title' in request.POST:
            data = request.POST
            
            p = posts()
            
            p.creatorId = request.session.get('userId')
            p.categoryId = data['cat']
            p.title = data['title']
            p.body = data['body']
            p.tags = data['tags'].split("#")
            p.image = data['image']
            
            p.save()
            
            context = request.POST
            
            return render_to_response('grats.html',context)
        else:
            context = RequestContext(request, {'foo': 'bar',})
            return render_to_response('new.html',context,context_instance=RequestContext(request))
        
    else:
        return HttpResponseRedirect("/u/login")
    
def edit(request, blog_id):
    p = posts()
    user = users()
    if request.session.get('userId'):
        if 'title' in request.POST:
            data = request.POST
            
            p.creatorId = request.session.get('userId')
            p.categoryId = data['cat']
            p.title = data['title']
            p.body = data['body']
            p.tags = data['tags'].split("#")
            p.image = data['image']
            p.id = blog_id
            
            p.save()
            
            context = request.POST
            
            return render_to_response('grats.html',context)
        else:
            post = p.getPost(blog_id)
        
            context = RequestContext(request, {'blogId': blog_id,'postData' : post})
            return render_to_response('edit.html',context,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/u/login")
    
def delete(request, blog_id):
    p = posts()
    user = users()
    if request.session.get('userId'):
        isSU = user.isAdmin(request.session.get('userId'))
        
        if not isSU:
            return HttpResponseRedirect("/")
        
        p.deletePost(blog_id)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
    