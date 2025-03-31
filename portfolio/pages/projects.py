import reflex as rx
from rxconfig import config
from portfolio.routes import PageRoutes, PageTitles


@rx.page(route=PageRoutes.projects , title=PageTitles.projects)
def projects() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
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


app = rx.App()
app.add_page(projects)
