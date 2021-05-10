from django.shortcuts import render
from django.http import HttpResponse
# import Http Response from django 
from django.shortcuts import render 
from polls.models import Stocks, Stocks_Articles, Processing_Control, Logging
from django.conf import settings
from datetime import datetime
import requests
from lxml import html
from bs4 import BeautifulSoup

class Stock_Result:
    def __init__(self, stock_ticker, stock_name, last_price, volume, exchange, article_text, article_date, creation_datetime, istodayarticle):
        self.stock_ticker = stock_ticker
        self.stock_name = stock_name
        self.last_price = last_price
        self.volume = volume
        self.exchange = exchange
        self.article_text = article_text
        self.article_date = article_date
        self.creation_datetime = creation_datetime
        self.istodayarticle = istodayarticle


   
# create a function 
def home_view(request): 
    # create a dictionary to pass 
    # data to the template 
    context ={ 
        "data":"Gfg is the best", 
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    } 
    # return response with template and context 
    return render(request, "index.html", context)


def nasdaq_earnigs_view(request): 
    # create a dictionary to pass 
    # data to the template 
    context ={ 
        "data":"Gfg is the best", 
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    } 
    # return response with template and context 
    return render(request, "nasdaq_earnigs.html", context)


def teste_view(request): 
    # create a dictionary to pass 
    # data to the template 
    context ={ 
        "data":"Gfg is the best", 
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    } 
    # return response with template and context 
    return render(request, "teste.html", context)



def bio_catalysts_view(request): 
    #stock_list = Stocks.objects.values('stock_ticker', 'stock_name', 'last_price', 'volume')
    #stock_list = Stocks_Articles.objects.select_related()
    #stock_list = Stocks.objects.all().select_related().values('stock_ticker', 'stock_name', 'last_price', 'volume')
    
    Stocklist = []
 
    
    obj_all_stocks = Stocks.objects.all()
    for obj_stocks in obj_all_stocks:
        article = Stocks_Articles.objects.all().filter(stock_ticker=obj_stocks.stock_ticker).order_by('-creation_datetime').first()
        
        istodayarticle = False
        


        if article:
            #if article date is today
            if datetime.now().date() == article.article_date:
                istodayarticle = True

            Stocklist.append( Stock_Result(obj_stocks.stock_ticker, obj_stocks.stock_name, obj_stocks.last_price, obj_stocks.volume, obj_stocks.exchange, article.article_text, article.article_date, article.creation_datetime, istodayarticle))
        else:
            Stocklist.append( Stock_Result(obj_stocks.stock_ticker, obj_stocks.stock_name, obj_stocks.last_price, obj_stocks.volume, obj_stocks.exchange, '', '', '', istodayarticle))

    #Sort list by article date
    StocklistNew = sorted(Stocklist, key=lambda Stock_Result: str(Stock_Result.article_date), reverse=True)

    
    context_dict = {'stocks': StocklistNew}

    # return response with template and context 
    return render(request, "bio_catalysts.html", context_dict)



def stock_details_view(request, i_stock_ticker): 

    stock_atual_price = getInformation(i_stock_ticker)
    
    stock_information = Stocks.objects.all().filter(stock_ticker=i_stock_ticker).values('stock_ticker', 'stock_name', 'exchange', 'sector', 'industry', 'last_price', 'volume', 'businessSummary').first()
    
    # Today's articles
    today_articles = Stocks_Articles.objects.all().filter(stock_ticker=i_stock_ticker, article_date__gte= datetime.now().date()).order_by('-creation_datetime')
    

    # History of all articles
    articles_history = Stocks_Articles.objects.all().filter(stock_ticker=i_stock_ticker, article_date__lt= datetime.now().date()).order_by('-creation_datetime')

    context_dict = {'stock_information': stock_information,
                    'all_articles': articles_history,
                    'today_articles': today_articles,
                    'stock_atual_price': stock_atual_price }

    # return response with template and context 
    return render(request, "stock_details.html", context_dict)




def purgeLogging_view(request): 

    Logging.objects.all().delete()
    Processing_Control.objects.all().delete()

    return HttpResponse("Deleted all data from Logging table.")


def getInformation(i_stock_ticker):
    
    try:
        url = 'https://finance.yahoo.com/quote/' + i_stock_ticker

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        #print(result.content.decode())
        html_content = result.content.decode()
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup)

        quote_header = soup.find('div', attrs={'id':'quote-header-info'})


        stock_atual_price = quote_header.find('span', attrs={'data-reactid':'32'})
        #print(stock_atual_price.text)
        return stock_atual_price.text


    except Exception:
            print("Entrou na excepção getStockPriceYahoo...")
            pass
    

#def getTeste(i_stock_ticker):
#    
#    try:
#        url = 'https://finance.yahoo.com/quote/' + i_stock_ticker + '/profile'
#
#        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#        result = requests.get(url, headers=headers)
#        #print(result.content.decode())
#        html_content = result.content.decode()
#        soup = BeautifulSoup(html_content, 'html.parser')
#        #print(soup)
#
#        businessSummary_panel = soup.find('section', attrs={'class':'quote-sub-section Mt(30px)'})
#        businessSummary = businessSummary_panel.find('p')
#
#        print(businessSummary.text)
#
#        obj = Stocks.objects.get(stock_ticker=i_stock_ticker)
#        obj.businessSummary = businessSummary.text.replace("'", "''")
#        obj.save()
#
#
#    except Exception:
#        print("Entrou na excepção getStockPriceYahoo...")
#        pass

