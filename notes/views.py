from django.shortcuts import render, redirect
from .models import Subject, Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        subject_name = request.POST['subject']
        subject, _ = Subject.objects.get_or_create(name=subject_name)
        Note.objects.create(title=title, content=content, subject=subject)
        return redirect('note_list')
    return render(request, 'notes/note_form.html')

def note_edit(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        subject_name = request.POST['subject']
        note.subject, _ = Subject.objects.get_or_create(name=subject_name)
        note.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'note': note})