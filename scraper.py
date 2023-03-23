import requests
import re

URL = 'http://127.0.0.1:8000/price/all'

def get_minimum_price(user_product):
    try:
        product_list = requests.get(URL).json()
    except:
        return '\nThe server is not available at the moment, please try again later.'
    else:
        pattern = re.compile(user_product, re.IGNORECASE)
        product = [e for e in product_list if re.search(pattern, e['product'])]
        min_price = False
        min_price_product = dict()

        if len(product) > 0:
            for x in product_list:
                if x['product'] == product[0]['product']:
                    if not min_price:
                        min_price = x['price']
                        min_price_product.clear()
                        min_price_product = x.copy()
                    else:
                        if x['price'] < min_price:
                            min_price = x['price']
                            min_price_product.clear()
                            min_price_product = x.copy()
    
            return min_price_product
        else:
            return '\nNo matching products found.'

if __name__ == '__main__':
    user_product = input('Enter the name of the product\n')
    result = get_minimum_price(user_product)

    if type(result) == dict:
        print('\nHere is the best price for your product\n')
        print(f'Product: {result["product"]}\nPrice: {result["price"]}\nStore: {result["store"]}')
    else:
        print(result)
