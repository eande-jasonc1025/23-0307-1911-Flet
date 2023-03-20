import plotly.graph_objects as go

import flet
from flet import Page
from flet.plotly_chart import PlotlyChart

# Create random data with numpy
import numpy as np

def main(page: Page):

    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                        mode='lines',
                        name='lines'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                        mode='lines+markers',
                        name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                        mode='markers', name='markers'))
    
    page.add(PlotlyChart(fig, expand=True))

    ##jwc o fig.show()

flet.app(target=main)