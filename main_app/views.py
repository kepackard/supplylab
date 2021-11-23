from django.shortcuts import render
# ----- Authentication -----
from django.contrib.auth import login

# todo - delete once no longer needed
from django.http import HttpResponse



# ========== GENERAL Views ==========
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ========== AUTHENTICATION Views ==========


# ========== CLASSROOM Views ==========
# todo - added here simply to verify authentication working - either:
# 1. keep (add an actual html template with content & update the view function)
# -- or -- 
# 2. remove & change out the LOGIN_REDIRECT_URL on settings.py to a different url
def classroom_index(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


# ========== WISHLIST Views (i.e., - associate item with classroom) ==========


# ========== ITEM Views ==========



