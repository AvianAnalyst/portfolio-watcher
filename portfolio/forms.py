from django import forms
from datetime import date
from .models import Investment, Company


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name',)


class DateInput(forms.DateInput):
    input_type = 'date'


class InvestmentEntryForm(forms.ModelForm):

    class Meta:
        model = Investment
        fields = ('purchase_date', 'company', 'cost', 'num_of_shares')
        widgets = {
            'purchase_date': DateInput,
        }
