from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import PartyRegistrationForm

def home(request):
    """
    Displays the home page.
    """
    return render(request, 'home.html')

def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = PartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'login.html')
        else:
            form = PartyRegistrationForm()
        return render(request, 'registration.html', {'form': form})

def about(request):
    """
    Renders the 'about' page.
    """
    return render(request, 'about.html')

def leadership(request):
    """
    Renders the 'leadership' page.
    """
    return render(request, 'leadership.html')

def login_view(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user credentials
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Login the user
                login(request, user)
                
                # Redirect the user to the "blogs" page
                return redirect('blogs')  # Replace 'blogs' with the appropriate URL name
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def blogs(request):
    """
    Renders the 'blogs' page.
    """
    return render(request, 'blogs.html')
