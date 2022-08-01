from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from Awww.Awww.models import MusicPost

def index(request):
    return render(request, 'index.html')

#플레이리스트 좋아요
def MusicPostLike(request, pk):
    post = get_object_or_404(MusicPost, id = request.POST.get('musicpost_id'))
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.like.add(request.user)
    
    return HttpResponseRedirect(reverse('musicpost-detail', args=[str(pk)]))
    