import pandas as pd


WebsiteLink = "https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_records_and_statistics"

scraper = pd.read_html(WebsiteLink)

# for i in enumerate(scraper):
#     print("--------------------------")
#     print(i)


print(scraper[2])

df = scraper[2]
df.to_excel(r'Data\1.3_Yearly_IPL_Position.xlsx', index=False)
