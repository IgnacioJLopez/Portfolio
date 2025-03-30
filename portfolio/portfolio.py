import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Ignacio J López", size="9"),
            rx.text(
                "Data Scientist | Machine Learning Engineer | Python Developer",
                font_size="2xl",
                font_weight="bold",
                text_color="gray.500",
                text_align="center",
                margin_bottom="4",
            ),
            rx.link(
                rx.button("Check my LinkedIn"),
                href="https://www.linkedin.com/in/igjlopez/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )


app = rx.App()
app.add_page(index)
