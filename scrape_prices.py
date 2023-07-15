import requests
from bs4 import BeautifulSoup

def scrape_amazon_price(url):
    # Headers are set to mimic a real web browser. This can sometimes help to avoid bot detection mechanisms.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en-US,en;q=0.9", 
        "Connection": "keep-alive", 
        "Referer": "https://www.google.com/"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_soup = BeautifulSoup(response.content, 'html.parser')
        print(html_soup)
        price_whole = html_soup.select_one('div#ppd span.a-price-whole')
        price_fraction = html_soup.select_one('div#ppd span.a-price-fraction')

        if price_whole and price_fraction:
            price = float(price_whole.get_text().replace(',', '') + '.' + price_fraction.get_text())
            print('The price of the item is €', price)
        else:
            print('Price not found')
    else:
        print('Failed to fetch the page')

# Example usage
scrape_amazon_price('https://www.amazon.fr/r%C3%A9paration-RealPlus-magn%C3%A9tiques-douverture-Smartphones/dp/B09F8N3M4V')
