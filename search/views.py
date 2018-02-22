from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

from django.shortcuts import render
#from .filters import UserFilter

from functools import reduce
import operator

class SearchProductView(ListView):
    template_name = "search/view.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        vegetarian = request.GET.get('vegetarian')
        gluten_free = request.GET.get('gluten_free')
        category = request.GET.get('category')
        print(category)

        result = Product.objects.all()
        
        if query:
            query_list = query.split(' ')
            print(query_list)
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            )
        if vegetarian:
            result = result.filter(vegetarian = True)
        if gluten_free:
            result = result.filter(gluten_free = True)
        if category:
            result = result.filter(category = category)
            #result = result.filter(category = category.title())

        return result