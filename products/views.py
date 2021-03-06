from __future__ import unicode_literals

from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product, Food, Beverage
from locations.models import Location
from model_utils.managers import InheritanceManager

# Featured List/Detail Views

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

# List Views (Class & FBV)
class ProductListView(ListView):
    template_name = "products/list.html"
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Food.objects.all()
        #return Product.objects.select_subclasses(Food)#all()

def product_list_view(request):
    queryset = Product.objects.select_subclasses(Food)#all()
    context = {
        'object_list': queryset
    }
    return Food.objects.all()
    #return render(request, "products/list.html", context)

# Detail Views (Class & FBV) + Slug Detail View
class ProductDetailSlugView(DetailView):
    #queryset = Product.objects.all()
    queryset = Product.objects.select_subclasses()
    #template_name = "products/detail.html"
    template_name = "products/detail.html"
    
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Oh no!")
        
        return instance


class ProductDetailView(DetailView):
    template_name = "products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.select_subclasses().get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    
    instance = Product.objects.select_subclasses().get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)

# class ProductCreateView(ProductCreateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy('person_changelist')

# def load_options(request):
#     category_id = request.GET.get('category')
#     cities = City.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})
    
    