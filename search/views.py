from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter

class SearchProductView(ListView):
    template_name = "search/view.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.all()
            
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})