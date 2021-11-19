from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login

def signup(req) :
    form = NewUserForm()

    if req.method == 'POST' :
        form = NewUserForm(req.POST)
        if form.is_valid() :
            user = form.save()
            login(req, user)
            return redirect('home')
    else : 
        form = NewUserForm()

    return render(req, 'signup.html', {'form': form})