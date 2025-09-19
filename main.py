"""import requests
url= "https://restcountries.com/v3.1/all?fields=name"
odgovor=requests.get(url)
drzave=odgovor.json
dr=[]

for d in drzave[:5]:
    dr.append(d.get("name").get("official"))

for d in dr:
    c=requests.get(f"https://restcountries.com/v3.1/all?fields=name{d}").json()
    print(c[0].get("capital"))"""


import requests

url = "https://restcountries.com/v3.1/all?fields=name"
odgovor = requests.get(url)
drzave = odgovor.json()
dr = []

for d in drzave[:67]:
    dr.append(d.get("name").get("official"))

for d in dr:
    c = requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
    print(c[0].get("capital")[0])



url = "https://api.waifu.pics/sfw/waifu"
odgovor = requests.get(url)

if odgovor.status_code == 200:
    data = odgovor.json()
    print("Ali bi raje to:", data.get("url"))
else:
    print("Puko si:", odgovor.status_code)


url = "https://api.waifu.pics/sfw/waifu"
data = requests.get(url).json()

print("Ali to:", data["url"])




url = "https://catfact.ninja/fact"
data = requests.get(url).json()

print("Kitty😼:", data["fact"])


url="https://api.waifu.pics/sfw/waifu"
data=requests.get(url).json()
print("Prava maca😸:", data["url"])

