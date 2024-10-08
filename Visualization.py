import pandas as pd
from WebScraping import CompanyInfoWebScraping

company_names_lst, company_ticker_lst, market_cap_lst, categories_for_company_lst = CompanyInfoWebScraping('https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/','https://companiesmarketcap.com/apple/marketcap/')
print(company_names_lst, company_ticker_lst, market_cap_lst, categories_for_company_lst)
data = dict()

lst = [company_names_lst, company_ticker_lst, market_cap_lst, categories_for_company_lst]
names = ["company_names", "company_stock_ticker", "company_mkt_cap", "company_categories"]

for i in range(len(lst)):
    data[names[i]] = lst[i]

df = pd.DataFrame(data=data)
df.head(25)