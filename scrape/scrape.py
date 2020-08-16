import datetime
import requests
from requests_html import HTML
import os

n = datetime.datetime.now()
y = n.year

def url_to_txt(url, filename=f"world-{y}.html", save = False):
    r=requests.get(url)
    if r.status_code == 200:
        html_text=r.text
        if save:
            with open(filename, 'w') as f:
                f.write(html_text)
        return html_text
    return ""


url = 'https://www.boxofficemojo.com/year/world/?ref_=bo_nb_yl_tab'

r = requests.get(url)

html_text = url_to_txt(url)
r_html = HTML(html = html_text)
table_class = ".imdb-scroll-table"
r_table=r_html.find(table_class)
table_data = []
header_names = []

if len(r_table) == 1:
    parse_table = r_table[0]
    rows = parse_table.find("tr")
    header = rows[0]
    header_col = header.find('th')
    header_names = [x.text for x in header_col]

    for row in rows[1:]:
        cols = row.find("td")
        row_data = []

        for i, x in enumerate(cols):
            row_data.append(x.text)
        table_data.append(row_data)

print(header_names)
print(table_data[0])