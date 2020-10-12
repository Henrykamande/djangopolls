
from django.http import HttpResponse
# Create your views here.



def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('dj4e_cookie', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))

    resp.set_cookie('dj4e_cookie', 'c5383525') # No expired date = until browser close
    resp.set_cookie('dj4e_cookie', 'c5383525' , max_age=1000) # seconds until expire
    return resp

def sessfun(request) :

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count='+str(num_visits))

