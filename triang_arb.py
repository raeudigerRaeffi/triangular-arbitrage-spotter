import krakenex

fee = 0.0026
pair=[['XXBTZUSD', 'XETHZUSD', 'XETHXXBT'], ['XXBTZUSD', 'EOSUSD', 'EOSXBT'], ['XXBTZUSD', 'XXLMZUSD', 'XXLMXXBT'], ['XXBTZUSD', 'BCHUSD', 'BCHXBT'], ['XXBTZUSD', 'DASHUSD', 'DASHXBT'], ['XXBTZUSD', 'GNOUSD', 'GNOXBT'], ['XXBTZUSD', 'XETCZUSD', 'XETCXXBT'], ['XXBTZUSD', 'XREPZUSD', 'XREPXXBT'], ['XXBTZEUR', 'XETHZEUR', 'XETHXXBT'], ['XXBTZEUR', 'EOSEUR', 'EOSXBT'], ['XXBTZEUR', 'XXLMZEUR', 'XXLMXXBT'], ['XXBTZEUR', 'BCHEUR', 'BCHXBT'], ['XXBTZEUR', 'DASHEUR', 'DASHXBT'], ['XXBTZEUR', 'GNOEUR', 'GNOXBT'], ['XXBTZEUR', 'XETCZEUR', 'XETCXXBT'], ['XXBTZEUR', 'XREPZEUR', 'XREPXXBT']]


k = krakenex.API()


def k_trading_pair(a1):
    a_1 = k.query_public('Ticker',{"pair" : a1[0] })
    a_2 = k.query_public('Ticker',{"pair" : a1[1] })
    a_3 = k.query_public('Ticker',{"pair" : a1[2] })
    return [a_1["result"],a_2["result"],a_3["result"]]

def calc_arb(a1,a2,a3):
    
    way1 = (1 * float(a1["b"][0]) * float(a3["b"][0]) / float(a2["a"][0])) * (1-fee)**3
    way2 = (1 * float(a2["b"][0]) / float(a3["a"][0]) / float(a1["a"][0])) * (1-fee)**3
    
  
    print("way1: " +str(way1-1)+"%")
    print("way2: " +str(way1-1)+"%")
  

while True:
    for x in pair:
        pairs = k_trading_pair(x)
        print(x)
        calc_arb(pairs[0][x[0]],pairs[1][x[1]],pairs[2][x[2]])
    
