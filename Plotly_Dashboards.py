# dcc e html módulos específicos do Dash para criar componentes HTML e interativos
# plotly.graph_objects criia gráficos interativos
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


# Um objeto Dash é criado para representar a aplicação web
app = Dash(__name__)

# O layout da aplicação é definido, incluindo um título, uma mensagem, um menu suspenso (dcc.Dropdown) e um gráfico (dcc.Graph)
app.layout = html.Div([
    html.H4('Interactive color selection with simple Dash example'),
    html.P("Select color:"),
    dcc.Dropdown(
        id="dropdown",
        options=['Gold', 'MediumTurquoise', 'LightGreen'],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

# Funcao de callback
# A função display_color é chamada sempre que o valor do menu suspenso é alterado
# O argumento color é o valor selecionado no menu suspenso.
# A função cria um gráfico de barras (go.Bar) com cores determinadas pelo valor selecionado no menu suspenso.
@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], # substituir pela sua própria fonte de dados
                    marker_color=color))
    return fig

# Servidor web é iniciado
app.run_server(debug=True)