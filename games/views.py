from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.

def games_list(request):
    return render(request, 'games/games_list.html', {})


#def games_list(request):
#    return HttpResponse("We could put anything here")
#    return HttpResponse(request.user.username)