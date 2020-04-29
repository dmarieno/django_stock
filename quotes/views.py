# David Marieno code

from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

def home(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        # pk_8987020b7a0b4522bb0bcb3816a97092
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_8987020b7a0b4522bb0bcb3816a97092")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'ticker': "Enter a ticker symbol above"})


def about(request):
    return render(request,'about.html',{})

def addStock(request):
    import requests
    import json

    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('addStock')

    else:
        ticker = Stock.objects.all()
        stock_list = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_8987020b7a0b4522bb0bcb3816a97092")
            try:
                api = json.loads(api_request.content)
                stock_list.append(api)
            except Exception as e:
                api = "Error..."

        return render(request,'addStock.html',{'ticker': ticker, "stock_list": stock_list})

def delete(request,ticker_id):
    item_to_be_deleted = Stock.objects.get(pk=ticker_id)
    item_to_be_deleted.delete()
    messages.success(request,("Stock Has Been Deleted!"))
    return redirect(addStock)

def deleteStock(request):
    ticker = Stock.objects.all()
    return render(request, 'deleteStock.html', {'ticker': ticker})
