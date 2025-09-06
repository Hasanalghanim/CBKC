from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout,authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
import json



@ensure_csrf_cookie

def check_auth(request):
    print("Session Data:", request.session)
    if request.user.is_authenticated:
        return JsonResponse({
            'is_authenticated': True,
            'username': request.user.username,
        })
    else:
        return JsonResponse({'is_authenticated': False})
    
@csrf_protect

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)




@require_POST
@ensure_csrf_cookie

def login_view(request):
    try:
        data = json.loads(request.body)
        print(data)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # creates session cookie
            return JsonResponse({'success': True, 'username': user.username})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)







def dashboard(request):
    return render(request, "dashboard.html",)

