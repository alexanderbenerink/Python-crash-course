import urllib.request, json
import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
w_logger = logging.getLogger('wisselkoers')
w_handler = logging.StreamHandler()
w_formatter = logging.Formatter('%(asctime)s - (%(name)s) - %(levelname)s - %(message)s')
w_handler.setFormatter(w_formatter)
w_logger.addHandler(w_handler)
w_logger.setLevel(logging.DEBUG)

class CurrecyConverter:
    mijn_valuta:str
    valuta_symbool:str
    code:str
    symbol:str
    wisselkoers:float
    
    def __init__(self, mijn_valuta:str, valuta_symbool:str, code:str, symbol:str, rate:float) -> None:
        self.code = code
        self.symbol = symbol
        self.rate = rate
        self.mijn_valuta = mijn_valuta
        self.valuta_symbool = valuta_symbool
        
        # w_logger.debug(f'Nieuwe wisselkoers: {self}')
    
    def update_wisselkoers(self, rate:float) -> None:
        self.rate = rate
        
    def convert_to(self, amount:float) -> float:
        return amount * self.rate
    
    def __str__(self) -> str:
        return f'{mijn_valuta} ({valuta_symbool}) -> {self.code} ({self.symbol}): {self.rate}'
    

if __name__ == '__main__':
    mijn_valuta = "EUR"
    valuta_symbool = "€"
    
    currency_code = "GBP"
    currency_symbol = "£"
    
    with urllib.request.urlopen(f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{mijn_valuta.lower()}.json") as exchange_url:
        data = json.load(exchange_url)
    
    wisselkoers = data[mijn_valuta.lower()][currency_code.lower()]
    aantal_geld = 100
    
    converter = CurrecyConverter(mijn_valuta, valuta_symbool, currency_code, currency_symbol, wisselkoers)
    print(f"Begin aantal: {aantal_geld}")
    print(converter)
    print(f"Converted: {converter.convert_to(aantal_geld)}")
    converter.update_wisselkoers(wisselkoers * 1.1)
    print(f"Converted + updated wisselkoers(x1.1): {converter.convert_to(aantal_geld)}")
    