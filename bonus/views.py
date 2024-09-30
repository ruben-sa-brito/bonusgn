from django.shortcuts import render
from .models import SaleRange, SalesRanges
def home_page(request):
    return render(request, 'home.html')


def view_bonus(request):
    try:
        sales_ranges = SalesRanges.objects.get(active_ranges=True)
    except:
        return render(request, 'home.html', {'not_found': f'Nenhuma bonificação ativa, contate o administrador'})
    sales_ranges_related = sales_ranges.sale_range.all()
    value = float(request.POST['value'].replace('.','').replace(',','.').replace('R$',''))
    for x in sales_ranges_related:
        if '-' not in x.sale_range: break
        if value <= float(x.sale_range.split('-')[1].replace(',','.')):
            if x.value == 0: return render(request, 'home.html', {'value': 'Voce não atingiu o valor mínimo necessário =('})
            return render(request, 'home.html', {'value': f'Sua bonificação: R$ {x.value}0'})
    if sales_ranges.active_percentage:
        return render(request, 'home.html', {'value':'Incrível! Sua bonificação: R$ ' + str(int(value * (sales_ranges_related.last().value)/100)) + '.00'})
    
    return render(request, 'home.html', {'value': f'Incrível! Sua bonificação: R$ {sales_ranges_related.last().value}. '})
    