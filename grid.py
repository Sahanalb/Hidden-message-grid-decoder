import requests
from bs4 import BeautifulSoup
def printGrid(url_1):
    request_data =  requests.get(url_1)

    data_1 = []
    soup_1 = BeautifulSoup(request_data.text,"html.parser")
    all_rows = soup_1.find_all('tr')
    for row in all_rows[1:]:
        each_col = row.find_all('td')
        if len(each_col) == 3:
            x = int(each_col[0].text.strip())
            character = each_col[1].text.strip()
            y = int(each_col[2].text.strip())
            data_1.append([character,x,y])

    max_x = max(x for _, x, _ in data_1)
    max_y = max(y for _, y, _ in data_1)

    grid_1 = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
    for character,x,y in data_1:
        grid_1[y][x] = character

    for row in grid_1:
        print("".join(row))


url_1 = "https://docs.google.com/document/d/e/2PACX-1vSIuj8yOWnYunQsp2OfY9yrZzVIzNE0Z0mpQ7v73VVgYPE4R4kFaTmIE5HAt3Fr3S58aEokVNwTGrWt/pub"
printGrid(url_1)




