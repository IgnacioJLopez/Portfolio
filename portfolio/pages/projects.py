import reflex as rx
from rxconfig import config
from portfolio.routes import PageRoutes, PageTitles
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv"
)

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(
    contours_z=dict(
        show=True,
        usecolormap=True,
        highlightcolor="limegreen",
        project_z=True,
    )
)
fig.update_layout(
    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
    margin=dict(l=65, r=50, b=65, t=90),
)


def mountain_surface():
    return rx.center(
        rx.plotly(data=fig),
    )

@rx.page(route=PageRoutes.projects , title=PageTitles.projects)
def projects() -> rx.Component:

    plot_section = rx.center(
        rx.plotly(data=fig),
    )

    # Welcome Page (Index)
    projects_section = rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Ignacio J López", size="9"),
            rx.text(
                "Here I will put my projects",
                font_size="2xl",
                font_weight="bold",
                text_color="gray.500",
                text_align="center",
                margin_bottom="4",
            ),
            rx.text(
                "If only I had some",
                font_size="lg",
                text_align="left",
                margin_bottom="8",
            ),
            spacing="6",
            justify="center",
            align="start",
            min_height="85vh",
        )
        
    )

    return rx.box(
        projects_section,
        plot_section,
        width="100%",
    )

