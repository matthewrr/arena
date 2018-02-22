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
        category = request.GET.get('category')
        course = request.GET.getlist('course')
        diet = request.GET.getlist('diet')
        beverage_type = request.GET.getlist('beverage_type')
        alcohol_type = request.GET.getlist('alcohol_type')
        serving_type = request.GET.getlist('serving_type')
        
        #vegetarian = request.GET.get('vegetarian')
        #gluten_free = request.GET.get('gf')
        print(category)
        print(course)

        result = Product.objects.all()
        
        print(result)
        
        if query:
            query_list = query.split(' ')
            print(query_list)
            
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            )

        #result = result.filter(Q(course__icontains=course))
        if category != 'all' and category != 'All':
            result = result.filter(Q(category__icontains=category))
            
        if course:
            result = result.filter(
                reduce(operator.or_,
                    (Q(course__icontains=q) for q in course))
            )   
        if diet:
            result = result.filter(
                reduce(operator.or_,
                    (Q(diet__icontains=q) for q in diet))
            )   
        if beverage_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(beverage_type__icontains=q) for q in beverage_type))
            )   
        if alcohol_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(alcohol_type__icontains=q) for q in alcohol_type))
            )   
        if serving_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(serving_type__icontains=q) for q in serving_type))
            )        

        return result