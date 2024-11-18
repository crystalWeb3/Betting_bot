import requests
import time

url = "https://platform.tonybet.lv/api/event/list?isTopLive_eq=1&competitor2Id_neq=&competitor1Id_neq=&status_in[]=2&status_in[]=1&oddsExists_eq=1&main=1&limit=30&relations[]=odds&relations[]=league&relations[]=result&relations[]=competitors&relations[]=players&relations[]=sportCategories&relations[]=broadcasts&relations[]=statistics&relations[]=additionalInfo&relations[]=withMarketsCount&relations[]=tips&period=0&lang=en"

def fetch_tonybet ():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() 
        data = data.get("data", {})
        
        items = data.get("items", [])
        
        relations = data.get("relations", [])
        odds = relations.get("odds", {})
        
        footballs = []
        
        for i in range(len(items)):
            item = items[i]
            id = item.get("id", 0)            
            if id:            
                odd_lists = odds.get(str(item["id"]))
                odd1 = odd2 = 0
                for odd in odd_lists:
                    if odd.get('id') == 621:
                        outcomes = odd.get("outcomes", [])
                        if len(outcomes):
                            odd1 = outcomes[0]["odds"]
                            odd2 = outcomes[1]["odds"]
                
                football = {
                    'id': item.get("id"),
                    'time': item.get("time"),
                    'name': item.get("translationSlug"),
                    "odd1": odd1,
                    "odd2": odd2
                }
                # print(str(football['id']) + " " + football['time'] + " " + football['name'] + " " + str(football['odd1']) + " " + str(football['odd2']))
                footballs.append(football)
        return footballs
            
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []
