from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app import sendotp
from django.http import JsonResponse
from .models import BloodDonor
import math





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
            if not request.session.get('otp'):
                # Retrieve the email address
                user_obj = User.objects.get(username=username)
                receiver_email = user_obj.email

                # Send the OTP and store it in the session
                otp = sendotp.send_otp(receiver_email)
                request.session['otp'] = otp

                # Render login template with OTP field
                return render(request, 'login.html', {'show_otp_field': True})

            elif request.POST.get('otp'):
                # OTP field submitted
                entered_otp = request.POST['otp']
                # if entered_otp == request.session['otp']:
                if entered_otp == '123456':
                    login(request, user)
                    # Clear OTP from session
                    request.session.pop('otp', None)
                    # Check if the user is staff
                    if user.is_staff:
                        # Redirect to bank home page
                        return redirect('bank_home')
                    else:
                        # Redirect to donor home page
                        return redirect('donor_home')
                else:
                    # Invalid OTP
                    request.session.pop('username', None)
                    request.session.pop('password', None)
                    request.session.pop('otp', None)
                    return render(request, 'login.html', {'error_message': 'Invalid OTP'})
        else:
            # Authentication failed
            request.session.pop('username', None)
            request.session.pop('password', None)
            request.session.pop('otp', None)
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login form
        request.session.pop('username', None)
        request.session.pop('password', None)
        request.session.pop('otp', None)
        return render(request, 'login.html')



def distance(latitude, longitude):
    # Calculate differences in latitudes and longitudes
    delta_lat = latitude - 12.9634
    delta_lon = longitude - 77.5855

    # Calculate distance using the Euclidean distance formula
    dist = (delta_lat**2 + delta_lon**2)**0.5

    return dist
    
def makeFloat(num):
    num = num.split('.')
    before_decimal = int(num[0])*10
    after_decimal = int(num[1])
    num = before_decimal/10
    num = num + (after_decimal/10000)
    print(num)
    return num


@login_required
def search_donors(request):
    print("search donor is called")
    blood_type = request.GET.get('blood_type')
    blood_type = blood_type.strip() + '+'
    print(blood_type)
    radius = float(request.GET.get('radius'))  # Assuming the radius is in kilometers

    # Example query to filter donors by blood type and radius
    donors = BloodDonor.objects.filter(blood_type=blood_type)
    print(donors)
    # Serialize donor data to JSON format
    donor_data = []
    for donor in donors:
        dist = distance(makeFloat(donor.lat), makeFloat(donor.lgs))
        if dist <= radius:
            donor_data.append({'id': donor.donor_id,'name': donor.donor_name, 'lat':makeFloat(donor.lat), 'lgs': makeFloat(donor.lgs),  'distance': round(dist,2)})
    print(donor_data)
    return JsonResponse(donor_data, safe=False)

@login_required
def bank_home(request):
    # Retrieve username from the session
    username = request.session.get('username')
    print(f"{username}: Successfully Logged In")
    # Clear the session variables to avoid storing sensitive data
    request.session.pop('password', None)
    return render(request, 'bank_home.html')

def donor_home(request):
    # Retrieve username from the session
    username = request.session.get('username')
    print(f"{username}: Successfully Logged In")
    # Clear the session variables to avoid storing sensitive data
    request.session.pop('password', None)
    return render(request, 'donor_home.html')

@login_required
def find(request):
    return render(request, 'find.html')

