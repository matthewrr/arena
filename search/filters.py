from django.contrib.auth.models import User
from products.models import Product
import django_filters

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
   
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    #    widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['title', 'description']
        #fields = ['username', 'first_name', 'last_name', 'year_joined', 'groups']