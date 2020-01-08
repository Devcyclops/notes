
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Note

note = Note()



def home(request):
    all_notes = Note.objects.all()
    return render(request, 'home.html',{'notes':all_notes}) 



def make_notes(request):
    if request.method == 'POST':
        notes = request.POST['note']
        data = {
            'status':''
        }
        note.saved_note = notes
        note.save()
        data['status'] = '200'

        return JsonResponse(data)
    return render(request, 'home.html')

        
def make_note(request):
    if request.method == 'POST':
        notes = request.POST['note']
        note.saved_note = notes
        note.save()
        

        return redirect('note:home')
    return render(request, 'home.html')
        