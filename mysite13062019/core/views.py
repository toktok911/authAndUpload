from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

def home(request):
	return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

@login_required 
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #dictionary key here is the name of the input in the html template

        print(uploaded_file.name)
        print(uploaded_file.size)

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file) 
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)

        
    return render(request, 'upload.html')