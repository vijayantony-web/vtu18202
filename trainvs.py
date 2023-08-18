from datetime import date as d
from bs4 import BeautifulSoup
import requests

def getdata(url):
    r=requests.get(url)
    return r.text 
    
from_st=input("Enter Start Station: ")
to_st=input("Enter Destination Station: ")
date=str(d.today())
date_s=date.split("-")
date_s=date_s[::-1]
date=""
for i in date_s:
    date+=i+"-"
date=date[:-1]


url="https://www.railyatri.in/booking/trains-between-stations?from_name="+from_st+"+JN+&journey_date="+date+"&src=tbs&to_name="+to_st+"+JN+&user_id=-1692321191&user_token=61692321191&utm_source=tt_dwebhome_search"

htmldata=getdata(url)

soup=BeautifulSoup(htmldata,'html.parser')
data_str=""
for item in soup.find_all("div",class_='customDivTbs Result_Section'):
    data_str+=item.get_text()
    
result=data_str.split("\n")
print("Trains between "+from_st +" to "+to_st)
print("")

for i in result:
    if i!=" ":
        print(i,end=" ")
    if 'Availability' in i:
        print()
