import time
from tonybet import fetch_tonybet
from x3000 import fetch_x3000
import re

def makeListFromName(name) :
    cleaned_text = re.sub(r'\(.*?\)', '', name)
    cleaned_text = cleaned_text.lower()
    
    print(cleaned_text)
    words = [word for word in cleaned_text.split() if word]
    sorted_words = sorted(words, key=len, reverse=True)
    
    return sorted_words
    

def main() :    
    tonybet_data = fetch_tonybet()
    if tonybet_data:
        for tb in tonybet_data:
            print(f"{tb['name']}  {tb['time']} {tb['odd1']} {tb['odd2']}")
    else:
        print("No data retrieved.")
        
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    
    x3000_data = fetch_x3000()
    if x3000_data:
        for xd in x3000_data:
            print(f"{xd['name']} {xd['time']} {xd['sport']}")
    else:
        print("x3000 No data")
        
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        
if __name__ == "__main__":
    main()