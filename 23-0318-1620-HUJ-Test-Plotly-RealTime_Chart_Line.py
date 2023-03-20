import time
import plotly.graph_objects as go
import numpy as np

import flet as ft

def main(page: ft.Page):

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))  # white noise 1
    nse2 = np.random.randn(len(t))  # white noise 2

    # Two signals with a coherent part at 10Hz and a random part
    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    fig = go.FigureWidget()
    fig.add_scatter()
    fig

    data = [1,3,2,4,3,3,2,3]

    for i in range(len(data)):
        time.sleep(0.3)
        with fig.batch_update():
            fig.data[0].y = data[:i]


###jwc y ft.app(target=main)
###jwc y ft.app(target=main, view=ft.WEB_BROWSER, port=5000)
ft.app(target=main)
###jwc y ft.app(target=main, view=ft.WEB_BROWSER, port=5000)