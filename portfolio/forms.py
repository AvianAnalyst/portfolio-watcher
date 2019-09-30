from django import forms
from .models import Investment, Company


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name',)


class InvestmentEntryForm(forms.ModelForm):

    class Meta:
        model = Investment
        fields = ('purchase_date', 'company', 'cost', 'num_of_shares')


class DateInput(forms.DateInput):
    input_type = 'date'


class PortfolioRequestForm(forms.Form):
    investment_date = forms.DateField(label='investments date', widget=DateInput)
