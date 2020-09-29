import pandas as pd
from plotnine import *
wdi = pd.read_csv("wdi_small_tidy_2015.csv")
col_list=["Mortality rate, infant (per 1,000 live births)",'GDP per capita (constant 2010 US$)',"Country Name"]
gdp = wdi.loc[:,col_list]
(ggplot(gdp, aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)'))+geom_point()
)