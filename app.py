#https://community.plot.ly/t/running-dash-app-in-docker-container/16067
#https://plot.ly/~jackp/17555/#/code
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from core import core
server=flask.Flask(__name__)
app = dash.Dash(__name__,server=server)
#server = app.server
data=core()
userList=data.df.keys()
#datatypeList=data.df[userList[0]]["duration"].keys()
datatypeList=["total","compile","other"]
#x=data.x
#y=data.y['total']
#x=['2020-03-01-14h20','2020-03-02-16h20','2020-03-11-09h20','2020-03-11-17h20']
#y=[73,23,12,17]
colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash Application',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(id='display-value', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(id='my-graph'),
    html.Div([
      dcc.Dropdown(
        id='dropdown-user',
        options=[{'label': i, 'value': i} for i in userList],
        value='user1'
      )],style={'width': '48%', 'float': 'left', 'display': 'inline-block'}),
    html.Div([
      dcc.Dropdown(
        id='dropdown-type',
        options=[{'label': i, 'value': i} for i in datatypeList],
        value='total'
      )],style={'width': '48%', 'float': 'left', 'display': 'inline-block'})
#    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('my-graph','figure'),
             [dash.dependencies.Input('dropdown-user', 'value'),dash.dependencies.Input('dropdown-type', 'value')])

def update_figure(user,dataType):
  #x=data.x
  #y=data.y[dataType]
  x=data.df[user]["delivery"]
  y=data.df[user]["duration"][dataType]
  return {
            'data': [
              {'x':x,'y':y,'type': 'bar', 'name': dataType}
            ],
            'layout': {
              'plot_bgcolor': colors['background'],
              'paper_bgcolor': colors['background'],
              'font': {
                'color': colors['text']
              },
              'yaxis':{'title':"Elapsed time [min]"}
            }
          }


"""
@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
"""
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050,debug=False)
