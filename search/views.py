from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Beverage, Food
from locations.models import Location

from django.shortcuts import render
from django.db import models
#from .filters import UserFilter
from model_utils.managers import QueryManager

from functools import reduce
import operator

#title, description, price, location, image, slug, active, featured
#beverage: comapny, company_location,beverage_type, alcohol_type, abv, ibu, serving_type
#food: course, dietary_restrictions



class SearchProductView(ListView):
    template_name = "search/view.html"
    
    def get_queryset(self, *args, **kwargs):
        
        request = self.request
        
        query = request.GET.get('q')
        category = request.GET.get('category')
        
        # food
        course = request.GET.getlist('course')
        #about = About.objects.get(id=1)
        dietary_restrictions = request.GET.getlist('diet')
        #beverage
        company = request.GET.get('company')
        company_location = request.GET.get('company_location')
        beverage_type = request.GET.getlist('beverage_type')
        alcohol_type = request.GET.getlist('alcohol_type')
        serving_type = request.GET.getlist('serving_type')
        ibu = request.GET.get('ibu')
        abv = request.GET.get('abv')
        
        #result = Product.objects.select_subclasses()


        
        #result = Food.objects.filter(course=course)
        # for i in result:
        #     print(isinstance(i,Food))
        # print(result)

        # result = Food.objects.filter(
        #         reduce(operator.or_,
        #               (Q(course__icontains=q) for q in course))
        #     )
        
        result = Food.objects.all()
        food = Food.objects.all()
        
        if course:
            food = food.filter(
                reduce(operator.or_, (Q(course__icontains=q) for q in course))
            )
        if dietary_restrictions:
            food = food.filter(
                reduce(operator.and_, (Q(diet__icontains=q) for q in dietary_restrictions))
            )
        
        print(food)
        print(dietary_restrictions)
        for item in food:
            print(item.diet)

        #print(course)
  
        #if course:
        #    result = result.filter(item.course="appetizer")
        #return result
        # if category == 'food' or category == 'all':
        #     if course:
        #         result = result.filter(
        #             reduce(operator.or_,
        #                 (Q(course__icontains=q) for q in course))
        #         )   
        #     if dietary_restrictions:
        #         result = result.filter(
        #             reduce(operator.or_,
        #                 (Q(dietary_restrictions__icontains=q) for q in dietary_restrictions))
        #         )
            
        
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
        if category != 'all' and category != 'All' and category:
            result = result.filter(Q(category__icontains=category))
        
        # if dietary_restrictions:
        #     result = result.filter(
        #         reduce(operator.or_,
        #             (Q(dietary_restrictions__icontains=q) for q in dietary_restrictions))
        #     )    .select_subclasses()
        
        #result = Product.objects.select_subclasses(Food)
        # if course:
        #     result = result.filter(
        #         reduce(operator.or_,
        #             (Q(course__icontains="appetizer") for q in course))
        #     )
        if beverage_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(beverage_type__icontains=q) for q in beverage_type))
            ).select_subclasses()
        
        if alcohol_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(alcohol_type__icontains=q) for q in alcohol_type))
            ).select_subclasses()   
        if serving_type:
            result = result.filter(
                reduce(operator.or_,
                    (Q(serving_type__icontains=q) for q in serving_type))
            ).select_subclasses()        

        return food