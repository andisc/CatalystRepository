from django.conf import settings
import requests
from lxml import html
from bs4 import BeautifulSoup

from datetime import date, datetime



def main():

    try:
        url = 'https://finance.yahoo.com/quote/BNTC' 

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        #print(result.content.decode())
        html_content = result.content.decode()
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup)

        #table = soup.find('table', attrs={'class':'nirtable collapse-table news-table'})
        ##print(table)
        #table_body = table.find('tbody')
        #rows = table_body.find_all('tr')
#
        #columns = rows[0].find_all('td')
        #v_article_date = columns[0].text.lstrip().rstrip()
#
        ##if the process find any article with the today date
        #if(validateday(v_article_date)):
        #    article_desc = columns[1].find('div', attrs={'class':'nir-widget--field nir-widget--news--headline'})
        #    print("URL: " + article_desc.a.get('href'))
        #    print("DESCRIPTION: " + article_desc.text.lstrip().rstrip())
        #    now = datetime.now()
        #    print("ARTICLE_DATE: " + str(now))

    except Exception:
            print("Entrou na excepção getStockPriceYahoo...")
            pass
    
        
 
if __name__ == "__main__":
    main()
