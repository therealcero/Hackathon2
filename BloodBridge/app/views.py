from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        if request.session.get('username') and request.session.get('password'):
            # Username and password already stored in session
            username = request.session['username']
            password = request.session['password']
        else:
            # Retrieve username and password from the POST request
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Store username and password in the session
            request.session['username'] = username
            request.session['password'] = password
        
        # Your authentication logic here
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful
            if request.POST.get('otp'):
                # OTP field submitted
                entered_otp = request.POST['otp']
                if entered_otp == '123456':  # Replace with your OTP verification logic
                    login(request, user)
                    # Redirect to the home page
                    return redirect('home')
                else:
                    # Invalid OTP
                    request.session.pop('username', None)
                    request.session.pop('password', None)
                    return render(request, 'login.html', {'error_message': 'Invalid OTP'})
            else:
                # OTP field not submitted, render login template with OTP field
                return render(request, 'login.html', {'show_otp_field': True})
        else:
            # Authentication failed
            request.session.pop('username', None)
            request.session.pop('password', None)
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login form
        request.session.pop('username', None)
        request.session.pop('password', None)
        return render(request, 'login.html')
        

@login_required
def home(request):
    # Retrieve username from the session
    username = request.session.get('username')
    print(f"{username}: Successfully Logged In")
    # Clear the session variables to avoid storing sensitive data
    request.session.pop('password', None)
    return render(request, 'home.html')

@login_required
def find(request):
    return render(request, 'find.html')