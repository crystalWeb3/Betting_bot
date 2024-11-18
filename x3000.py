import requests

url = "https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/event/live/open.json?lang=lv_LV&market=LV&client_id=2&channel_id=1&ncid=1731503164995"

def fetch_x3000():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        
        liveEvents = data.get("liveEvents", [])
        
        x3000_datas = []
        
        for i in range(len(liveEvents)):
            data = liveEvents[i]
            englishName = data['event']['englishName']
            sport = data['event']['sport']
            
            liveData = data.get('liveData', {})
                    
            matchClock = liveData.get('matchClock', {})
            time = f"{matchClock.get('minute', 'N/A')}:{matchClock.get('second', 'N/A')}"
                    
            scoreData = liveData.get('score', {})
            score = f"{scoreData.get('home', 'N/A')}:{scoreData.get('away', 'N/A')}"
                    
            betOffer = data.get('mainBetOffer', {'outcomes': []})
            outcomes = betOffer.get('outcomes', [])
            
            odddata = []
            for j in range(len(outcomes)):
                oddName = outcomes[j].get('englishLabel', 'N/A')
                oddValue = outcomes[j].get("odds", 'N/A')
                odddata.append ({
                    "name": oddName,
                    "value": oddValue
                })
            
            x3000_datas.append({
                "name": englishName,
                "sport": sport,
                "time": time,
                "score": score,
                "odddata": odddata
            })
        return x3000_datas                        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []
