from django.shortcuts import render
from .models import SaleRange, SalesRanges

def home_page(request):
    sales_ranges = SalesRanges.objects.filter(active_ranges=True)
    return render(request, 'home.html', {'sales_ranges':sales_ranges})

def bonus_page(request, bonus_id):
    sales_ranges = SalesRanges.objects.get(pk=bonus_id)
    return render(request, 'bonus.html', {'bonus_id': bonus_id, 'bonus_name':sales_ranges.bonus_name})

def view_bonus(request, bonus_id):
    
    sales_ranges = SalesRanges.objects.get(pk=bonus_id)
    
    sales_ranges_related = sales_ranges.sale_range.all()
    value = float(request.POST['value'].replace('.','').replace(',','.').replace('R$',''))
    for x in sales_ranges_related:
        if '-' not in x.sale_range: break
        if value <= float(x.sale_range.split('-')[1].replace(',','.')):
            if x.value == 0: return render(request, 'bonus.html', {'value': 'Voce não atingiu o valor mínimo necessário =('})
            return render(request, 'bonus.html', {'value': f'Sua bonificação: R$ {x.value}0'})
    if sales_ranges.active_percentage:
        return render(request, 'bonus.html', {'value':'Incrível! Sua bonificação: R$ ' + str(int(value * (sales_ranges_related.last().value)/100)) + '.00', 'bonus_id':bonus_id, 'bonus_name':sales_ranges.bonus_name})
    
    return render(request, 'bonus.html', {'value': f'Incrível! Sua bonificação: R$ {sales_ranges_related.last().value}. ', 'bonus_id':bonus_id, 'bonus_name':sales_ranges.bonus_name})
    