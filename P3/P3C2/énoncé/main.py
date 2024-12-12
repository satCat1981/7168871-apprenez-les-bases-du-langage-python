from bs4 import beautifulSoupe


with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
