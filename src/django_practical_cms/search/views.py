

from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render_to_response

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
        
    return render_to_response('search/search.html',
                              {'query':query,
                               'results' : results ,
                               }
                            )
    #===========================================================================
    # results = FlatPage.objects.filter(content__icontains=query)
    # template = loader.get_template('search/search.html')
    # context = Context({'query' : query, 'result' : results})
    # response = template.render(context)
    # return HttpResponse(response)
    #===========================================================================
    