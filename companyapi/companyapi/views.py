from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested")
    friends = [
        'Ameeray',
        'Mana',
        'Don'

    ]
    return JsonResponse(friends, safe=False)