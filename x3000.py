import requests

url = "https://eu-offering-api.kambicdn.com/offering/v2018/pafx3lv/event/live/open.json?lang=lv_LV&market=LV&client_id=2&channel_id=1&ncid=1731503164995"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse JSON data
    
    liveEvents = data.get("liveEvents", [])
    for i in range(len(liveEvents)):
        data = liveEvents[i]
        englishName = data['event']['englishName']
        sport = data['event']['sport']
        
        liveData = data.get('liveData', {})
        
        # Safely retrieve minute and second from matchClock if they exist
        matchClock = liveData.get('matchClock', {})
        time = f"{matchClock.get('minute', 'N/A')}:{matchClock.get('second', 'N/A')}"
        
        # Safely retrieve home and away scores if they exist
        scoreData = liveData.get('score', {})
        score = f"{scoreData.get('home', 'N/A')}:{scoreData.get('away', 'N/A')}"
        
        # Safely retrieve mainBetOffer and outcomes
        betOffer = data.get('mainBetOffer', {'outcomes': []})
        outcomes = betOffer.get('outcomes', [])
        
        odddata = ""
        for j in range(len(outcomes)):
            oddName = outcomes[j].get('englishLabel', 'N/A')
            oddValue = outcomes[j].get("odds", 'N/A')
            odddata += f"{oddName}:{oddValue} / "
                
        print(f"{englishName} | {sport} | {time} | {score} | {odddata}")
        
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
