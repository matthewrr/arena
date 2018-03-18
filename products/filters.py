from django.contrib.admin.filters import AllValuesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'products/admin/dropdown_filter.html'