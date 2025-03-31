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
            rx.text(
                "Turning data into action.",
                font_size="lg",
                text_align="left",
                margin_bottom="8",
            ),
            rx.hstack(
                rx.button(
                    "My Projects",
                    color_scheme="indigo",
                    size='4',
                    variant="outline",
                    radius="large",
                    on_click=rx.redirect("/projects")
                ),
                rx.button(
                    "About Me",
                    color_scheme="amber",
                    size='4',
                    variant="outline",
                    radius="large",
                    on_click=rx.redirect("/about"),
                ),
                rx.button(
                    "Contact Me",
                    color_scheme="indigo",
                    size='4',
                    variant="outline",
                    radius="large",
                    on_click=rx.redirect("/contact"),
                ),
                spacing="5"
            ),
            spacing="6",
            justify="center",
            align="start",
            min_height="85vh",
        )
        
    )


app = rx.App()
app.add_page(index)
