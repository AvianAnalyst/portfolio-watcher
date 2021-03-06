from django.http import HttpResponseRedirect as Redirect
from django.http import JsonResponse
from django.shortcuts import render

from portfolio.forms import *
from .models import Company, Investment


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def create_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return Redirect('/create/investment')
    else:
        form = AddCompanyForm()
        return render(request, 'add_company.html', {'form': form})


def create_investment(request):
    if request.method == 'POST':
        form = InvestmentEntryForm(request.POST)
        if form.is_valid():
            form.save()
            company = form.cleaned_data.get('company', 'error')
            shares = form.cleaned_data.get('num_of_shares', 'error')
            message = f'Thanks, your entry for {company} with {shares} shares was entered!'
            return render(request, 'invest.html', {'form': form, 'message': message})
    else:
        form = InvestmentEntryForm()
        return render(request, 'invest.html', {'form': form})


def get_portfolio(request):
    requested_date = request.GET.get('investment_date', date.today())
    info_date = request.GET.get('info_date', date.today())
    data = []
    companies = Company.objects.all()
    for company in companies:
        entry = {'company': company.name}
        try:
            investment = Investment.objects.filter(company=company,
                                                   purchase_date__lte=requested_date,
                                                   entry_date__lte=info_date).order_by('-purchase_date',
                                                                                       '-entry_date')[0]
            entry['quantity'] = investment.num_of_shares
            entry['cost'] = investment.cost
            data.append(entry)
        except IndexError:
            pass
    return JsonResponse(data, safe=False)
