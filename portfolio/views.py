from django.http import HttpResponseRedirect as Redirect
from django.http import JsonResponse
from django.shortcuts import render
from datetime import date

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
            company = form.cleaned_data.get('company', 'error')
            shares = form.cleaned_data.get('num_of_shares', 'error')
            message = f'Thanks, your entry for {company} with {shares} shares was entered!'
            return render(request, 'invest.html', {'form': form, 'message': message})
    else:
        form = InvestmentEntryForm()
        return render(request, 'invest.html', {'form': form})


def get_portfolio(request):
    requested_date = request.GET.get('investment_date', date.today())
    data = []
    companies = Company.objects.all()
    for company in companies:
        entry = {'company': company.name}
        try:
            investment = Investment.objects.filter(company=company, purchase_date__lte=requested_date).order_by('-purchase_date')[0]
            entry['quantity'] = investment.num_of_shares
            entry['cost'] = investment.cost
            data.append(entry)
        except IndexError:
            pass
    return JsonResponse(data, safe=False)


def retrieve(request):
    form = PortfolioRequestForm()
    return render(request, 'retrieve.html', {'form': form})
