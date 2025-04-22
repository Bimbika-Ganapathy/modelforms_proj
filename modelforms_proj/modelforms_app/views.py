from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ProjectForm

def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProjectForm()
    return render(request, 'submit_project.html', {'form': form})

def success(request):
    return render(request, 'success.html')


# Create your views here.
