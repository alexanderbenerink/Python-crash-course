import random
import logging
import re
import sqlite3
from functools import wraps

LOGLEVEL = logging.ERROR
b_logger = logging.getLogger('BANK')
b_logger.setLevel(LOGLEVEL)
b_handler = logging.StreamHandler()
b_formatter = logging.Formatter('%(asctime)s-(%(name)s)-%(levelname)s: %(message)s')
b_handler.setFormatter(b_formatter)
b_logger.addHandler(b_handler)

green_color = "\033[32m"
red_color = "\033[31m"
orange_color = "\033[33m"
reset_color = "\033[0m"


def my_logger(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        b_logger.error(f"Function '{func.__name__}' called with args: {args[-1]} and: {kwargs if kwargs else 'No kwargs'}")
        return func(*args, **kwargs)
    
    return wrapper

# ========================================
# Database connection
def database_connection(db_file:str, set_queries:list = [], get_queries:list = []):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"{green_color}Connected to {db_file}{reset_color}")
        cur = conn.cursor()
        
        with open('create_table.sql') as q_file:
            q = q_file.read()
            cur.execute(q)
        
        for query in set_queries:
            cur.execute(query)
        
        for query in get_queries:
            ex = cur.execute(query)
            print(ex.fetchall())
        
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
            print(f"{orange_color}Connection to {db_file} closed{reset_color}")

# ========================================
# ========================================

class EigenError(Exception):
    def __init__(self, msg, loglevel=LOGLEVEL):
        if loglevel > logging.WARNING:
            b_logger.error(f'Hoger dan Warning error: {msg}')
        super().__init__(msg)


class Rekening:
    rekeninghouder:str
    rekeningnummer:str
    saldo:float

    # @my_logger
    def __init__(self, rekeninghouder:str, saldo:float=0.0) -> None:
        self.rekeninghouder = rekeninghouder.upper()
        self.rekeningnummer = f'IBAN:{random.randint(10000000,99999999)}'
        self.saldo = saldo
        
        # b_logger.info(f'Nieuwe rekening: {self.rekeninghouder} [{self.rekeningnummer}], met beginsaldo: € {saldo:.2f}')


    # def __repr__(self) -> str:
    #     return f'{self.rekeninghouder} ({self.rekeningnummer}): € {self.saldo:.2f}'

    # @my_logger
    def overboeken(self, bedrag:float, tegenrekening:"Rekening") -> None:
        if tegenrekening.ontvangen(bedrag, self):
            self.saldo -= bedrag
        # else:
        #     print('Transactie mislukt')

    # @my_logger
    def ontvangen(self, bedrag:float, bron:"Rekening") -> bool:
        checksum = self.saldo + bedrag
        try: 
            self.saldo += bedrag
            # b_logger.info(f'€ {bedrag:.2f} ontvangen van {bron.rekeninghouder} [{bron.rekeningnummer}]')

            if self.saldo == checksum:
                # commit
                # b_logger.info(f'Nieuw saldo: € {self.saldo:.2f}')
                return True
            # else:
            #     b_logger.error(f'€ {bedrag:.2f} ontvangen van {bron.rekeninghouder} [{bron.rekeningnummer}] mislukt')
        except:
            print("Iets is misgegaan met de transactie")
        

class Spaarrekening(Rekening):
    rente:float

    def __init__(self, rekeninghouder: str, rente:float, saldo:float=0.0) -> None:
        super().__init__(rekeninghouder, saldo)
        self.rente = rente
        
        # b_logger.info(f'Spaarrekening: {self.rekeningnummer} met rente: {self.rente:.2f}')
    # @my_logger
    def overboeken(self, bedrag: float, tegenrekening: Rekening) -> None:
        if self.rekeninghouder == tegenrekening.rekeninghouder:
            # b_logger.info(f'Overboeken van spaarrekening naar betaalrekening {bedrag:.2f} -> {tegenrekening.rekeninghouder} [{tegenrekening.rekeningnummer}]')
            return super().overboeken(bedrag, tegenrekening)
        else:
            raise EigenError('Mag geen bedrag overboeken van een spaarrekening naar een rekening van een andere rekeninghouder')
    # @my_logger
    def ontvangen(self, bedrag: float, bron:Rekening) -> bool:
        try:
            if self.rekeninghouder == bron.rekeninghouder:
                # b_logger.info(f'€ {bedrag} ontvangen op spaarrekening van {bron.rekeninghouder} [{bron.rekeningnummer}]')
                return super().ontvangen(bedrag, bron)
            else:
                raise EigenError('Rekeninghouder komt niet overeen!')
        except:
            raise EigenError('Transactie mislukt')
    # @my_logger
    def krijgRente(self):
        self.saldo += self.rente * self.saldo
        # b_logger.info(f'Rente bijgeschreven: € {self.saldo:.2f}')


class Betaalrekening(Rekening):
    # @my_logger
    def storten(self, bedrag:float) -> None:
        self.saldo += bedrag
        # b_logger.info(f'€ {bedrag:.2f} gestort op {self.rekeninghouder} [{self.rekeningnummer}]')
    # @my_logger
    def opnemen(self, bedrag:float) -> None:
        if self.saldo > bedrag:
            self.saldo -= bedrag
            # b_logger.info(f'€ {bedrag:.2f} opgenomen van {self.rekeninghouder} [{self.rekeningnummer}], nieuw saldo: € {self.saldo:.2f}')
        else:
            raise EigenError('Te laag saldo!')

# ========================================
# recursive functions to check input
def check_name_input():
    name = input("Voer uw naam in: ")
    if all(name.isalpha() or name.isspace() for name in name):
        return name
    else:
        print("Naam mag alleen alphanumerieke tekens en spaties bevatten")
        return check_name_input()

def check_saldo_input():
    saldo = input("Voer uw saldo in: ")
    if re.match(r'^-?\d+(?:\.\d+)?$', saldo):
        return float(saldo)
    else:
        print("Saldo mag alleen numerieke tekens bevatten")
        return check_saldo_input()
# ========================================
# ========================================


if __name__ == '__main__':    
    # b1 = Betaalrekening(check_name_input())
    b1 = Betaalrekening('Peter Schols')
    # s1 = Spaarrekening(check_name_input(), check_saldo_input())
    s1 = Spaarrekening('Peter Schols', 0.01, 100)

    b2 = Betaalrekening('Tim Bolhoeve')
    s2 = Spaarrekening('Tim Bolhoeve', 0.05, 50)
    
    database_connection(
            db_file="testdb2.sqlite3",
            set_queries=[f"""INSERT INTO rekeningen_TimBolhoeve (rekeninghouder, rekeningnummer, saldo) 
                         VALUES ('{b1.rekeninghouder}', '{b1.rekeningnummer}', {b1.saldo});""",
                         f"""INSERT INTO rekeningen_TimBolhoeve (rekeninghouder, rekeningnummer, saldo) 
                         VALUES ('{s1.rekeninghouder}', '{s1.rekeningnummer}', {s1.saldo});""",
                         f"""INSERT INTO rekeningen_TimBolhoeve (rekeninghouder, rekeningnummer, saldo) 
                         VALUES ('{b2.rekeninghouder}', '{b2.rekeningnummer}', {b2.saldo});""",
                         f"""INSERT INTO rekeningen_TimBolhoeve (rekeninghouder, rekeningnummer, saldo)
                         VALUES ('{s2.rekeninghouder}', '{s2.rekeningnummer}', {s2.saldo});"""],
            get_queries=[f"SELECT * FROM rekeningen_TimBolhoeve;"]
    )
    
    b1.storten(1000)
    b1.overboeken(500, s1)
        
    s1.ontvangen(5, b1)

    #deze gaat fout! (of fout maken door s1->s2) want b1 kan alleen naar s1 overboeken
    b1.overboeken(1, s1)
    
    # set_queries=[f"UPDATE rekeningen_TimBolhoeve SET saldo = {b1.saldo} WHERE id = 1;",
    #                      f"UPDATE rekeningen_TimBolhoeve SET saldo = {s1.saldo} WHERE id = 2;",
    #                      f"UPDATE rekeningen_TimBolhoeve SET saldo = {b2.saldo} WHERE id = 3;",
    #                      f"UPDATE rekeningen_TimBolhoeve SET saldo = {s2.saldo} WHERE id = 4;"],
    database_connection(
            db_file="testdb2.sqlite3",
            set_queries=[f"UPDATE rekeningen_TimBolhoeve SET saldo = {b1.saldo} WHERE rekeninghouder = '{b1.rekeninghouder}';",
                         f"UPDATE rekeningen_TimBolhoeve SET saldo = {s1.saldo} WHERE rekeninghouder = '{s1.rekeninghouder}';",
                         f"UPDATE rekeningen_TimBolhoeve SET saldo = {b2.saldo} WHERE rekeninghouder = '{b2.rekeninghouder}';",
                         f"UPDATE rekeningen_TimBolhoeve SET saldo = {s2.saldo} WHERE rekeninghouder = '{s2.rekeninghouder}';"],
            get_queries=[f"SELECT * FROM rekeningen_TimBolhoeve;"]
    )
    
    # check per rekening of saldo > 0, en print de rekeninghouder, saldo en rekeningnummer
    rekeningen_list = [b1, s1, b2, s2]
    check_saldo = list(filter(lambda x: x.saldo > 0, rekeningen_list))
    
    print(f"{green_color}{[(x.rekeninghouder, x.saldo, x.rekeningnummer) for x in check_saldo]}{reset_color}")
    
    