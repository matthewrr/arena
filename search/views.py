from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from functools import reduce
from itertools import chain
import operator

from products.models import Product, Beverage, Food

#title, description, price, location, image, slug, active, featured
#beverage: comapny, company_location,beverage_type, alcohol_type, serving_type abv, ibu
#food: course, dietary_restrictions
class SearchProductView(ListView):
    template_name = "search/view.html"
    
    def get_queryset(self, *args, **kwargs):
        
        request = self.request
        query = request.GET.get('q')
        category = request.GET.get('category')
        
        course = request.GET.getlist('course')
        dietary_restrictions = request.GET.getlist('diet')
        beverage_type = request.GET.getlist('beverage_type')
        alcohol_type = request.GET.getlist('alcohol_type')
        serving_type = request.GET.getlist('serving_type')
        #company = request.GET.get('company')
        #company_location = request.GET.get('company_location')
        #ibu = request.GET.get('ibu')
        #abv = request.GET.get('abv')
        
        beverage = Beverage.objects.all()
        food = Food.objects.all()
        
        # for b in beverage:
        #     print(b.__class__.__name__)
        
        # for f in food:
        #     print(f.__class__.__name__)
        
        if query:
            query_list = query.split(' ')
            if category == 'food' or category == 'all':
                food = food.filter(
                    reduce(operator.and_,
                           (Q(title__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(description__icontains=q) for q in query_list))
                )
            if category == 'beverage' or category == 'all':
                beverage = beverage.filter(
                    reduce(operator.and_,
                           (Q(title__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(description__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(company__icontains=q) for q in query_list))
                )
        
        if category == 'food' or category == 'all': 
            if course:
                food = food.filter(
                    reduce(operator.or_, (Q(course__icontains=q) for q in course))
                )
            if dietary_restrictions:
                food = food.filter(
                    reduce(operator.and_, (Q(diet__icontains=q) for q in dietary_restrictions))
                )
        
        if category == 'beverage' or category == 'all':
            if beverage_type:
                beverage = beverage.filter(
                    reduce(operator.or_, (Q(beverage_type__icontains=q) for q in beverage_type))
                )
            if alcohol_type:
                beverage = beverage.filter(
                    reduce(operator.or_, (Q(alcohol_type__icontains=q) for q in alcohol_type))
                )
            if serving_type:
                beverage = beverage.filter(
                    reduce(operator.or_, (Q(serving_type__icontains=q) for q in serving_type))
                )
        
        #result_list = chain(food, beverage)
        
        if category == 'beverage':
            food = None
        if category == 'food':
            beverage = None
        
        
        return (food, beverage)
