#https://community.plot.ly/t/running-dash-app-in-docker-container/16067
#https://plot.ly/~jackp/17555/#/code
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from core import core

data=core()

def serve_layout():

  #update data from server
  data.update()

  userList=list(data.df.keys())
  datatypeList=list(data.df[userList[0]]["duration"].keys())
  #return dynamic html
  return html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='My Dash Application',
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
        value=userList[0]
      )],style={'width': '48%', 'float': 'left', 'display': 'inline-block'}),
    html.Div([
      dcc.Dropdown(
        id='dropdown-type',
        options=[{'label': i, 'value': i} for i in datatypeList],
        value=datatypeList[0]
      )],style={'width': '48%', 'float': 'left', 'display': 'inline-block'})
#    html.Div(id='display-value')
])

server=flask.Flask(__name__)
app = dash.Dash(__name__,server=server)
colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

#trick to have dynamic data plotted by Dash
app.layout = serve_layout

@app.callback(dash.dependencies.Output('my-graph','figure'),
             [dash.dependencies.Input('dropdown-user', 'value'),dash.dependencies.Input('dropdown-type', 'value')])

def update_figure(user,dataType):
  x=data.df[user]["delivery"]
  y=data.df[user]["duration"][dataType]
  print(x)
  print(y)
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

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050,debug=False)
