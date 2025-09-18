import requests

#baseUrl= "https://www.google.com/"
#klic = requests.get(baseUrl)

#print(klic)
#print(klic.text)

#atp klic - ne vraca HTML - vraca JSON, HML

#bseurl="https://api.chucknorris.io/jokes/random"
#call=requests.get(bseurl)
#print(call.text)
#ko smo 100%, da so podatki tipa JSON
#js=call.json()
#print(js.get("value"))

#import requests

#baseurle = "https://api.nationalize.io/?name="
#ime = "zaziy"

#klic = requests.get(baseurle + ime).json()
# print(klic)  # za pregled odgovora

#print(klic.get("count"))
#print(klic.get("name"))

#drzave = klic.get("country")  # samo shranimo, ne printamo

#for d in drzave:
    #print(d.get("country_id"), d.get("probability") * 100)





import webbrowser

#url = "https://i.waifu.pics/Tj6Wzwo.png"
#webbrowser.open(url)




url = "https://catfact.ninja/fact"

klic = requests.get(url).json()
print(klic.get("fact"))



dog_url = "https://dog-api.kinduff.com/api/facts?number=1"

dog_call = requests.get(dog_url).json()

dog_fact = dog_call.get("facts")
if dog_fact:
    print(dog_fact[0])
else:
    print("Fuck em nigadogs")

















    





