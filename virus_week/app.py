import pandas as pd
import folium
import numpy as np
def map_maker():
    import folium
    #url to the data
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-27-2020.csv'

    #read in data
    corona_df = pd.read_csv(url)
    lat1 = 34.223334
    long1 = -82.461707
    m = folium.Map(location = [lat1, long1], zoom_start=2, tiles = 'Stamen toner')
    folium.Circle(location = [lat1, long1], 
                  radius = 1000, 
                  color = 'red', 
                  fill = True).add_to(m)

    def circle_maker(x):
        folium.Circle(location = [x[0], x[1]], 
                  radius = float(np.max([x[2]*15, 20])), 
                  color = 'red', 
                  popup = f'<h5 style="backgroundcolor:black;fontcolor:white">{x[3]}</h5>\n<strong>Confirmed</strong>:  {x[2]}',
                  fill = True).add_to(m)

    corona_df[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].iloc[1:].apply(lambda x: circle_maker(x), axis = 1);
    return m._repr_html_()

def top_df_maker(n = 10, date=None):
    '''
    This function accepts a date and returns
    DataFrames with confirmed, death, recovered,
    and active information on top n countries.
    '''
    #getting the data and handling date
    import datetime
    now = datetime.datetime.now().strftime('%d-%m-%Y')
    if not date:
        try:
            date = now
            url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'
            corona_df = pd.read_csv(url)
        except:
            now = datetime.datetime.now()
            yesterday = datetime.timedelta(days = 1)
            yesterday_str = (now - yesterday).strftime('%m-%d-%Y')
            url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{yesterday_str}.csv'
            corona_df = pd.read_csv(url)
    else:
        url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'
        corona_df = pd.read_csv(url)
    #grouping and aggregating top n 
    cdf = corona_df.groupby('Country_Region').sum().nlargest(n, 'Confirmed')[['Confirmed']]
    ddf = corona_df.groupby('Country_Region').sum().nlargest(n, 'Deaths')[['Deaths']]
    rdf = corona_df.groupby('Country_Region').sum().nlargest(n, 'Recovered')[['Recovered']]
    adf = corona_df.groupby('Country_Region').sum().nlargest(n, 'Active')[['Active']]
    return {'cdf': cdf, 'ddf': ddf, 'rdf': rdf, 'adf': adf}
    
dfs = top_df_maker()
pairs = [(a, b) for a,b in zip(dfs['cdf'].index, dfs['cdf']['Confirmed'])]
cdf = dfs['cdf'].to_html()
cmap = map_maker()
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('df.html', frame = cdf, vmap = cmap, pairs = pairs)

if __name__ == '__main__':
    app.run(debug = True)