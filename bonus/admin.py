from django.contrib import admin
from .models import SaleRange, SalesRanges
from django.contrib import messages
from .forms import SalesRangesForm

class SaleRangeInline(admin.TabularInline):
    model = SaleRange  
    extra = 0  

# Define o admin para SalesRanges
class SalesRangesAdmin(admin.ModelAdmin):
    inlines = [SaleRangeInline] 
    list_display = ('bonus_name', 'active_ranges')
    fields = ['bonus_name','active_percentage', 'active_ranges']
    form = SalesRangesForm

admin.site.register(SalesRanges, SalesRangesAdmin)