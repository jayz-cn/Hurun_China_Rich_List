# scraping data from Hurun China Rich List

import requests
import json
import time


def scraping_hurun_china_rich_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'content-type': 'application/json',
        'referer': 'https://www.hurun.net/zh-CN/Rank/HsRankDetails?pagetype=rich'
    }

    base_url = 'https://www.hurun.net/zh-CN/Rank/HsRankDetailsList?num={}&search=&offset={}&limit=200' # 200 people per page

    # Each year has a different code for the url parameter 'num'
    years_code_total_page = {
        "2021": ["YUBAO34E", 15],
        "2019": ["XMTO3GFA", 10]
    }
    # "2020": "QWDD234E",
    # "2018": "DFW1O34E",
    # "2017": "RBN1E67E",
    # "2016": "HBF1E2E4",
    # "2015": "NNT76BFF",
    # "2014": "AQT76EYU",
    # "2013": "WHJ76EYU",
    # "2012": "LLL76MN7",
    # "2011": "LKI5ROP7",
    # "2010": "YKASROW3",
    # "2009": "BYUI24RD",
    # "2008": "BGTS23ED",
    # "2007": "LBWI56YU",
    # "2006": "GLH1523R",
    # "2005": "HHK1522P",
    # "2004": "HU58YT22",
    # "2003": "CUYU78QL",
    # "2002": "RT6URT2R",
    # "2001": "CV5RRTYQ",
    # "2000": "ZX2LRTYM",
    # "1999": "CUY998QL"

    # scrape data and save into a file
    with open('Hurun China Rich List.txt', 'a+', encoding='utf-8') as f:
        for year, (year_code, total_page) in years_code_map.items():
            for page in range(1, total_page+1):
                url = base_url.format(year_code, 200*(page-1))
                r = requests.get(url, headers=headers)

                if r.status_code == 200:
                    f.write(json.dumps(r.json(), ensure_ascii=False))
                    f.write('\n')
                    print("success: ", year, page)
                else:
                    print("request error: ", year, year_code, page)
                time.sleep(3)


if __name__ == "__main__":
    scraping_hurun_china_rich_list()
