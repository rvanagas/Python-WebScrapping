import requests, lxml
from bs4 import BeautifulSoup
import itertools
import xlsxwriter



page = 1
while page != 2:
    url = f"https://soshanger.com/epages/box11137.sf/en_GB/?ViewAction=FacetedSearchProducts&ObjectID=6114556&PageSize=60&SearchString=hanger&Page={page}"
    print(url)
    page = page + 1

    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    duomenu_arhyvas = []
    duomenu_arhyvas1 = []

    for title in soup.select(".TopPaddingWide"):
        duomenys = title.text
        nauji_duomenys = duomenys.strip()
        duomenu_arhyvas.append(nauji_duomenys)
        #print(duomenu_arhyvas)

    for price in soup.select(".price-value"):
        duomenys1 = price.text
        separator = '€'
        nauji_duomenys1 = duomenys1.rsplit(separator, 1)[0]
        duomenu_arhyvas1.append(nauji_duomenys1)
        #print(duomenu_arhyvas1)

#Create NumPy arrays


# Use concatenate() to join two arrays

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

array = duomenu_arhyvas1

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()

array1 = duomenu_arhyvas
for col, data in enumerate(array1):
    worksheet.write_column(row, col, data)







