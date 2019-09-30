from django.http import HttpResponseRedirect as Redirect
from django.http import JsonResponse
from django.shortcuts import render

from portfolio.forms import PortfolioRequestForm, InvestmentEntryForm, AddCompanyForm
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
            return Redirect('/investments')
    else:
        form = InvestmentEntryForm()
        return render(request, 'invest.html', {'form': form})


def get_portfolio(request):
    data = []
    companies = Company.objects.all()
    for company in companies:
        entry = {'company': company.name}
        try:
            investment = Investment.objects.filter(company=company).order_by('purchase_date')[0]
            entry['quantity'] = investment.num_of_shares
            entry['cost'] = investment.cost
        except IndexError:
            pass
            entry['quantity'] = 0
            entry['cost'] = 0
        data.append(entry)
    return JsonResponse(data, safe=False)


def retreive(request):
    form = PortfolioRequestForm()
    return render(request, 'retrieve.html', {'form': form})
