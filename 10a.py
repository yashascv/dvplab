import pandas as pd
import plotly.express as px
dollar_conv =pd.read_csv('CUR_DLR_INR.csv')
fig=px.line(dollar_conv,x='DATE',y='RATE',title="YASHAS-1KI23CS185-TIMESERIES")
fig.show()