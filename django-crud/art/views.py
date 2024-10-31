from django.http import JsonResponse
from django.shortcuts import render
from art.models import Art
from art.forms import ArtForm

def index(request):
    context = {}
    form = ArtForm()
    arts = Art.objects.all()
    context['arts'] = arts
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ArtForm(request.POST)
            else:
                arts = Art.objects.get(id=pk)
                form = ArtForm(request.POST, instance=arts)
            form.save()
            form = ArtForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            arts = Art.objects.get(id=pk)
            arts.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            arts = Art.objects.get(id=pk)
            form = ArtForm(instance=arts)
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    context['title'] = 'Contact'
    return render(request, 'contact.html', context)

def search(request):
    query = request.GET.get('query', '') 
    results = Art.objects.filter(name__icontains=query) 
    results_data = [{"id": art.id, "name": art.name} for art in results]
    return JsonResponse(results_data, safe=False)

def login(request):
    context = {}
    context['title'] = 'admin'
    return render(request, 'admin', context)

