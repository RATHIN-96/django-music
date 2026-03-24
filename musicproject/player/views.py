from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

def home(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'upload.html', {'form': form})