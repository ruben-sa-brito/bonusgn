from django.shortcuts import render
from .models import SaleRange, SalesRanges
def home_page(request):
    return render(request, 'home.html')


def view_bonus(request):
    sales_ranges = SalesRanges.objects.get(active_ranges=True)
    sales_ranges_related = sales_ranges.sale_range.all()
    value = float(request.POST['value'].replace('.','').replace(',','.').replace('R$',''))
    for x in sales_ranges_related:
        if '-' not in x.sale_range: break
        if value <= float(x.sale_range.split('-')[1].replace(',','.')):
            return render(request, 'home.html', {'value': f'R$ {x.value}0'})
    if sales_ranges.active_percentage:
        return render(request, 'home.html', {'value':'R$ ' + str(int(value * (sales_ranges_related.last().value)/100)) + '.00'})
    
    return render(request, 'home.html', {'value': sales_ranges_related.last().value})
    