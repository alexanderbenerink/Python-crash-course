import urllib.request, json, logging
from logger import custom_logger

customlogger: logging.Logger  = custom_logger()

class CurrencyConverter:
    def __init__(self, mijn_valuta, valuta_symbool, code, symbol):
        self._mijn_valuta: str = mijn_valuta
        self._valuta_symbool: str = valuta_symbool
        self._code: str = code
        self._symbol: str = symbol
        self._rate: float = self._getwisselkoers()

    def update_wisselkoers(self, new_rate: float) -> None:
        customlogger.debug('Updating wisselkoers')
        self._rate = new_rate

    def convert_to(self, amount: float) -> float:
        return amount * self._rate

    def __str__(self) -> str:
        return f"{self._mijn_valuta} {self._valuta_symbool} -> {self._code} {self._symbol}: {self._rate}"

    def _getwisselkoers(self) -> float:
        headers = {
            "Content-Type" : "application/json"
        }
        req = urllib.request.Request(url=f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{self._mijn_valuta.lower()}.json', headers=headers)
        response = urllib.request.urlopen(req)
        
        data = response.read()

        encoding = response.info().get_content_charset('utf-8')
        json_string = json.loads(data.decode(encoding))

        return float(json_string[self._mijn_valuta.lower()][self._code.lower()])
    
if __name__== "__main__":
    mijn_v = "EUR"
    mijn_s = "€"
    geld = 100

    code = "GBP"
    symbol = "£"
    
    converter: CurrencyConverter = CurrencyConverter(mijn_v, mijn_s, code, symbol)
    euro_to_pounds: float = converter.convert_to(geld)

    print(f"Origineel bedrag in euro's: {geld}€")
    print(f"Origineel bedrag in pond: {'%.2f' % euro_to_pounds}£")

    converter.update_wisselkoers(1.2)
    print(f"Origineel converted bedrag: {'%.2f' % euro_to_pounds}£ | Nieuw converted bedrag: {converter.convert_to(geld)}")
    print(converter)
