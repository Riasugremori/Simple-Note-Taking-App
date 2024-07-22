from django.shortcuts import render, get_object_or_404, redirect
from .models import SimpleNoteSecond

def index_views(request):
    notes = SimpleNoteSecond.objects.all()
    return render(request, 'index.html', {'notes': notes})

def Notes_view(request, title):
    note = get_object_or_404(SimpleNoteSecond, title=title) 
    return render(request, 'note_detail.html', {'note': note})  


def Add_view(request):
    if request.method == 'POST':
        new_notes = SimpleNoteSecond(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            date_created=request.POST.get('date_created'),
        )
        new_notes.save()
        return redirect('index')
    return render(request, 'add_notes.html')

def Edit_view(request, title):
    note = get_object_or_404(SimpleNoteSecond, title=title)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.date_created = request.POST.get('date_created')
        note.save()
        return redirect('notes', title=note.title)
    
    return render(request, 'edit_notes.html', {'note': note})


def Delete_view(request, title):
    note = get_object_or_404(SimpleNoteSecond, title=title)

    if request.method == 'POST':
        note.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'note': note})
