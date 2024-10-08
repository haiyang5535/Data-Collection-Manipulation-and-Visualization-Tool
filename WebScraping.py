import requests
from bs4 import BeautifulSoup

def CompanyInfoWebScraping(url, suburl):
    company_names_lst = []
    company_ticker_lst = []
    market_cap_lst = []
    categories_for_company_lst = []
    response = requests.get(url)
    print(response.status_code)
    print(response.headers.get('server'))

    soup = BeautifulSoup(response.text, "html.parser")
    market_cap_lst = soup.select(".name-td+ .td-right")
    total_lst = soup.select(".name-div")
    for tag in total_lst:
        company_names_lst.append(tag.a.div.string)
        company_ticker_lst.append(tag.a.select(".company-code")[0].text)
    total_lst[0]
    total_lst[0].find('a', href=True)['href']

    response2 = requests.get(suburl)
    print(response2.status_code)
    soup2 = BeautifulSoup(response2.text)
    industries = soup2.select('.categories-box .line1')

    industries_lst = []
    for element in industries[0].find_all("a"):
        industries_lst.append("".join(x for x in element.string.strip() if x.isalpha() or x == ' ').strip())
    industries_lst


    industries_lst = list()
    for company in total_lst:
        ind_list = list()
        add = company.find('a', href=True)['href']
        full_url = 'https://companiesmarketcap.com' + add
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text)
        industries = soup.select('.categories-box .line1')
        for element in industries[0].find_all("a"):
            ind_list.append("".join(x for x in element.string.strip() if x.isalpha() or x == ' ').strip())
        industries_lst.append(ind_list)
    return (company_names_lst, company_ticker_lst, market_cap_lst, categories_for_company_lst)


