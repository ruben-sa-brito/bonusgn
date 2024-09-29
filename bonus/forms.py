from django import forms
from .models import SalesRanges
from django.core.exceptions import ValidationError

class SalesRangesForm(forms.ModelForm):
    class Meta:
        model = SalesRanges
        fields = '__all__'

    def clean(self):    
        cleaned_data = super().clean()
        all_fields = self.data
        
        if self.instance and self.instance.pk:
            
            sales_range = self.instance
            if not sales_range.active_ranges and cleaned_data.get('active_ranges'):
                if len(SalesRanges.objects.filter(active_ranges=True)) == 1:
                    self.add_error('active_ranges', 'Já existe uma bonificação ativa')
                    raise ValidationError('Já existe uma bonificação ativa, é necessário desativá-la antes.')
        else:
            print(cleaned_data.get('active_ranges'))
            if cleaned_data.get('active_ranges'):
                if len(SalesRanges.objects.filter(active_ranges=True)) == 1:
                    self.add_error('active_ranges', 'Já existe uma bonificação ativa')
                    raise ValidationError('Já existe uma bonificação ativa, é necessário desativá-la antes.')

        ranges = list()
        k = list()
        errors = []
        for key in all_fields:
             if key.startswith('salerange_set') and key.endswith('sale_range'):
                ranges.append(all_fields[key])
                k.append(key)

        try: float(ranges[-2].replace(',','.'))
        except: errors.append('error')
        for i, value in enumerate(ranges[:-2]):
            
            try:
                val = value.split('-')
                val_1 = float(val[0].replace(',','.'))
                val_2 = float(val[1].replace(',','.'))
                if len(val) > 2: errors.append('error')
                if i == 0 and val_1 != 0:
                    errors.append('error')
                if val_1 >= val_2: errors.append('error')
            except:
                errors.append('error')
        
        values = [float(ranges[0].split('-')[1].replace(',','.'))]
        for rangel in ranges[1:-2]:
            values += [float(rangel.split('-')[0].replace(',','.')), float(rangel.split('-')[1].replace(',','.'))]
        total = 0.0
        values += [float(ranges[-2].replace(',','.'))]
        for i in range(0, len(values), 2):
            total += round(values[i+1] - values[i], 2)
            
        if total != 0.01 * (len(values)//2): errors.append('error')
        

        if errors:
            raise ValidationError('Algo deu errado com suas faixas de valores, por favor verifique e tente novamente.')
        

        
        return cleaned_data
