from django.shortcuts import render

def search_page(request):
    context = {
        'website_text': 'hello',
    }
    #print('hello')
    return render(request, "search/search.html", context)