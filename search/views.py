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
        category = request.GET.getlist('category')
        
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
        
        if query:
            query_list = query.split(' ')
            if not category or 'food' in category:
                food = food.filter(
                    reduce(operator.and_,
                           (Q(title__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(description__icontains=q) for q in query_list))
                )
            if not category or 'beverage' in category:
                beverage = beverage.filter(
                    reduce(operator.and_,
                           (Q(title__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(description__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(company__icontains=q) for q in query_list))
                )
        
        if not category or 'food' in category: 
            if course:
                food = food.filter(
                    reduce(operator.or_, (Q(course__icontains=q) for q in course))
                )
            if dietary_restrictions:
                food = food.filter(
                    reduce(operator.and_, (Q(diet__icontains=q) for q in dietary_restrictions))
                )
        
        if not category or 'beverage' in category:
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
        
        if category and 'beverage' not in category:
            beverage = None
        if category and 'food' not in category:
            food = None

        return (food, beverage)
