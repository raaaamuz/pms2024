# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser  # Import your CustomUser model
import json
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

# @csrf_exempt
# def user_login(request):
#     print("hioiiiiiiii")
#     if request.method == 'POST':
#         data = json.loads(request.body)
        
#         email = data.get('email')
#         password = data.get('password')
#         print(email, password)
#         try:
#             user = CustomUser.objects.get(email=email)
#             print(user)
#         except CustomUser.DoesNotExist:
#             return JsonResponse({'error': 'Invalid email or password'}, status=401)

#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Attempt to get the token for the user
#             try:
#                 token = Token.objects.get(user=user)
#             except ObjectDoesNotExist:
#                 # If token does not exist, create a new one
#                 token = Token.objects.create(user=user)
#             return JsonResponse({'success': True, 'username': user.get_username(), 'token': token.key})
#         else:
#             return JsonResponse({'error': 'Invalid email or password'}, status=401)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        email = data.get('email')
        password = data.get('password')
        print("Attempting to authenticate:", email, password)

        try:
            user = CustomUser.objects.get(email=email)
            print("User found:", user)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

        user = authenticate(request, username=email, password=password)  # Change to `username=email` if using email as username
        print("Authenticated user:", user)  # Debug print

        if user is not None:
            login(request, user)
            # Attempt to get the token for the user
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                # If token does not exist, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'success': True, 'username': user.get_username(), 'token': token.key})
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # List all existing users in the server log
        existing_users = CustomUser.objects.all()
        print("Existing users:")
        for user in existing_users:
            print("Username:", user.username, "Email:", user.email)

        # Check if email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'A user with this email already exists'}, status=400)
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'A user with this username already exists'}, status=400)

        # Create user using CustomUserManager's create_user method
        try:
            user = CustomUser.objects.create_user(email=email, username=username, password=password)
            print("User created:", user)  # Debug print to confirm user creation
            return JsonResponse({'success': True})
        except Exception as e:
            print("Error creating user:", e)  # Debug print to identify issues
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
