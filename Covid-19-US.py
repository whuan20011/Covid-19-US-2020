import  requests
from bs4 import BeautifulSoup
fout = open("Covid-19-US", "w")
result = requests.get("https://coronavirus.1point3acres.com/")
src = result.content
soup = BeautifulSoup(src)
countries = soup.find_all("div", class_ = "jsx-3737386991 stat row")
for country in countries:
    cur_country = country.find_all("span")
    res = [i.text for i in cur_country]
    print(",".join(res), file=fout)
        