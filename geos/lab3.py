import requests
import json
import matplotlib.pyplot as plt


# Question 1
rv = []

profile_urls = [
    'https://geosci.uchicago.edu/~kite/doc/geos28600_2020_lab_3/GEOS_38600_Lab_2_Profile_1.txt',
    'https://geosci.uchicago.edu/~kite/doc/geos28600_2020_lab_3/GEOS_38600_Lab_2_Profile_2.txt',
    'https://geosci.uchicago.edu/~kite/doc/geos28600_2020_lab_3/GEOS_38600_Lab_2_Profile_2.txt'    
    ]

for url in profile_urls:
    r = requests.get(url)
    txt = r.text
    txt = txt.split()
    rv.append(txt)

print(rv[0][3:])