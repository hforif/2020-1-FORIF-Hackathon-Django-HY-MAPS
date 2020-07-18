from django.shortcuts import render, redirect, Http404
from .models import Post, Board, Building

# Create your views here.

def writinglist(requests, number):
    postlist_data=[]
    board = Board.objects.get(building__number= number)
    postlist = Post.objects.filter(board= board)
    for post in postlist:
        postlist_data.append({
            "id":post.id,
            "title":post.title,
            "recent_revised_time":post.recent_revised_time
        })
    print(postlist_data)
    data = {
        "department":board.building.department,
        "postlist":postlist_data,
        "number":number
    }
    return render(requests, "writinglist.html", data)

def writingpost(requests, number):
    data = {
        "number":number,
    }
    if requests.method=="POST":
        building=Building.objects.get(number= number)
        board = Board.objects.get(building= building)
        post=Post(board=board)
        title=requests.POST.get("title", None)
        content=requests.POST.get("content", None)

        post.author = requests.user
        post.title=title
        post.contents=content
        post.save()
        return redirect("/posts/writinglist/"+str(number))
    return render(requests, "writingpost.html", data)

def writtencontent(requests, pk):
    # data={"number":number}
    post=Post.objects.get(id=pk)
    authority= False
    if requests.user == post.author:
        authority = True
        if requests.method=="POST":
            Post.objects.get(id=pk).delete()
            return redirect("/posts/writinglist/"+str(post.board.building.number))
    data = {
        "title": post.title, 
        "recent_revised_time": post.recent_revised_time, 
        "contents":post.contents,
        "author":post.author.username,
        "authority":authority,
        "pk":post.id,
        "number":post.board.building.number
    }
    return render(requests, "writtencontent.html", data)


def updatingpost(requests, pk):
    post=Post.objects.get(id= pk)
    
    if requests.user != post.author:
        raise Http404("unauthorized user")

    data = {
        "title":post.title,
        "contents":post.contents,
        "id":pk,
        "number":post.board.building.number
    }
    if requests.method=="POST":
        title=requests.POST.get("title", None)
        content=requests.POST.get("content", None)

        post.title=title
        post.contents=content
        post.save()
        return redirect("/posts/writinglist/"+str(post.board.building.number))
    return render(requests, "writingpost.html", data)
