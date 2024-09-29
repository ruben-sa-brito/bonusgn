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

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     ranges = list()
    #     for key in request.POST:
    #          if key.startswith('salerange_set') and key.endswith('sale_range'):
    #             ranges.append(request.POST[key])

    #     try: float(ranges[-2].replace(',','.'))
    #     except: form.add_error(None, 'Algo deu errado verifique os valores.')
    #     for i, value in enumerate(ranges[:-2]):
            
    #         try:
    #             val = value.split('-')
    #             val_1 = float(val[0].replace(',','.'))
    #             val_2 = float(val[1].replace(',','.'))
    #             if len(val) > 2: form.add_error(None, 'Algo deu errado verifique os valores.')
    #             if i == 0 and val_1 != 0:
    #                 messages.error(request, 'Valor inicial diferente de 0.')
    #                 return
    #             if val_1 >= val_2: form.add_error(None, 'Algo deu errado verifique os valores.')
    #         except:
    #             form.add_error(None, 'Algo deu errado verifique os valores.')
        
    #     values = [float(ranges[0].split('-')[1].replace(',','.'))]
    #     for rangel in ranges[1:-2]:
    #         values += [float(rangel.split('-')[0].replace(',','.')), float(rangel.split('-')[1].replace(',','.'))]
    #     total = 0.0
    #     values += [float(ranges[-2].replace(',','.'))]
    #     for i in range(0, len(values), 2):
    #         total += round(values[i+1] - values[i], 2)
            
    #     if total != 0.01 * (len(values)//2): form.add_error(None, 'Algo deu errado verifique os valores.')
        

    #     if form.is_valid():
    #         formset.save()
    #     else:
    #         messages.error(request, 'Algo deu errado com suas faixas de valores, por favor verifique e tente novamente.')
    #         return

admin.site.register(SalesRanges, SalesRangesAdmin)