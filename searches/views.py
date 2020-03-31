from django.shortcuts import render

from sve_app.models import Prime,BlogPostManager

from .models import SearchQuery

def search_view(request):
    query = request.GET.get('q', None)
    # author = None
    # if request.user.is_authenticated:
    #     # author = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(query=query)
        prime_list = Prime.objects.search(query=query)
        context['prime_list'] = prime_list
    
    return render(request, 'searches/view.htm',context)
