import reflex as rx
from rxconfig import config
from portfolio.routes import PageRoutes, PageTitles


def project_card(title: str, description: str, tech_stack: list) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(title, size="5"),
            rx.text(description),
            rx.flex(
                *[rx.badge(tech, variant="soft") for tech in tech_stack],
                flex_wrap="wrap",
                spacing="2",
            ),
            align="start", 
            spacing="3",
            padding="4"
        ),
        width="100%"
    )


@rx.page(route=PageRoutes.home, title=PageTitles.home)
def home() -> rx.Component:
    # index in te top rigth corner
    index_section = rx.hstack(
                rx.button(
                    "My Projects",
                    color_scheme="indigo",
                    size='4',
                    variant="ghost",
                    on_click=rx.redirect("/projects")
                ),
                rx.button(
                    "About Me",
                    color_scheme="amber",
                    size='4',
                    variant="ghost",
                    on_click=rx.redirect("/about"),
                ),
                rx.button(
                    "Contact Me",
                    color_scheme="indigo",
                    size='4',
                    variant="ghost",
                    on_click=rx.redirect("/contact"),
                ),
                spacing="5",
                justify="end",
                margin_top="40px",
                margin_right="40px",
            )

    hero_section = rx.hstack(
        rx.vstack(
            rx.heading(
                "Ignacio J López",
                size="9",
                style={
                    "margin_bottom": "-15px"
                },
            ),
            rx.text(
                "Data Scientist   |   Machine Learning Engineer   |   Python Developer",
                font_size="2xl",
                font_weight="bold",
                color_scheme="indigo",
                text_align="center",
                style={
                    "margin_bottom": "25px"
                },
            ),
            rx.text(
                "Welcome to my website built entirely with ",
                rx.code("Python!"),
                font_size="lg",
                text_align="left",
                color_scheme="orange",
                style={
                    "margin_bottom": "25px"
                },
            ),
            rx.text(
                "I build data-driven solutions that solve real-world problems and drive business impact.\n"
                "With over 7 years of experience transforming data into actionable insights, \nmy expertise combines a strong foundation in statistics, "
                "machine learning, \nand data engineering, complemented by a deep interest in solving business problems.",
                font_size="lg",
                text_align="left",
                margin_bottom="8",
                white_space="pre-wrap",
            ),
            spacing="6",
            justify="center",
            align="start",
            padding_y="16",
            min_height="85vh",
            max_width="1000px",
            margin_right="200px",
        ),
        rx.image(
            src="/images/anime_me_2.png",
            width="300px",
            height="auto",
            align="center",
            justify="center",
        ),
        justify="center",
        align="center",
        margin_bottom="100px",
    )

    # Timeline section
    timeline_section = rx.vstack(
        rx.heading(
            "My Professional Journey",
            size="7",
            margin_bottom="8",
            color_scheme="indigo",
        ),
        rx.box(
            rx.vstack(
                # 2024
                rx.hstack(
                    rx.box(
                        rx.text("2024", font_weight="bold", color_scheme="indigo", font_size="xl"),
                        width="15%",
                        text_align="right",
                        padding_right="4",
                    ),
                    rx.divider(orientation="vertical", height="auto"),
                    rx.box(
                        rx.vstack(
                            rx.heading("Senior Data Scientist", size="5", margin_bottom="1"),
                            rx.text("Frávega Tech"),
                            rx.text(
                                "Led the development of a predictive maintenance model that reduced equipment downtime by 35%. "
                                "Mentored junior data scientists and implemented MLOps best practices across the team.",
                                color="gray.600",
                            ),
                            align_items="start",
                            padding="4",
                            border_radius="lg",
                            background="gray.50",
                            margin_bottom="6",
                            width="100%",
                        ),
                        width="85%",
                    ),
                    align_items="flex-start",
                ),
                
                # 2023-2024
                rx.hstack(
                    rx.box(
                        rx.text("2023-2024", font_weight="bold", color_scheme="indigo", font_size="xl"),
                        width="15%",
                        text_align="right",
                        padding_right="4",
                    ),
                    rx.divider(orientation="vertical", height="auto"),
                    rx.box(
                        rx.vstack(
                            rx.heading("Data analyst", size="5", margin_bottom="1"),
                            rx.text("Spazios"),
                            rx.text(
                                "Responsible for developing and maintaining key automation processes to ensure a steady flow of leads." 
                                "Worked with databases and CRMs to extract, process, and analyse data using APIs, webhooks, and Python."
                                "Created interactive dashboards and reports in Power BI to support business decision-making.",
                                color="gray.600",
                            ),
                            align_items="start",
                            padding="4",
                            border_radius="lg",
                            background="gray.50",
                            margin_bottom="6",
                            width="100%",
                        ),
                        width="85%",
                    ),
                    align_items="flex-start",
                ),
                
                # 2021-2023
                rx.hstack(
                    rx.box(
                        rx.text("2021-2023", font_weight="bold", color_scheme="indigo", font_size="xl"),
                        width="15%",
                        text_align="right",
                        padding_right="4",
                    ),
                    rx.divider(orientation="vertical", height="auto"),
                    rx.box(
                        rx.vstack(
                            rx.heading("Physics Laboratory Technician", size="5", margin_bottom="1"),
                            rx.text("Physics Department Universidad de Buenos Aires"),
                            rx.text(
                                "Responsible for developing and maintaining key automation processes to ensure a steady flow of leads." 
                                "Worked with databases and CRMs to extract, process, and analyse data using APIs, webhooks, and Python."
                                "Created interactive dashboards and reports in Power BI to support business decision-making.",
                                color="gray.600",
                            ),
                            align_items="start",
                            padding="4",
                            border_radius="lg",
                            background="gray.50",
                            margin_bottom="6",
                            width="100%",
                        ),
                        width="85%",
                    ),
                    align_items="flex_start",
                ),
                
                # 2018-2020
                rx.hstack(
                    rx.box(
                        rx.text("2018-2025", font_weight="bold", color_scheme="indigo", font_size="xl"),
                        width="15%",
                        text_align="right",
                        padding_right="4",
                    ),
                    rx.divider(orientation="vertical", height="auto"),
                    rx.box(
                        rx.vstack(
                            rx.heading("Private Physics Educator", size="5", margin_bottom="1"),
                            rx.text("In-person and virtual"),
                            rx.text(
                                "Provided private tutoring in Physics and Mathematics to undergraduate students in Physics and related fields."
                                " Helped students improve their understanding of key concepts and succeed in their academic courses.",
                                color="gray.600",
                            ),
                            align_items="start",
                            padding="4",
                            border_radius="lg",
                            background="gray.50",
                            margin_bottom="6",
                            width="100%",
                        ),
                        width="85%",
                    ),
                    align_items="flex_start",
                ),
                
                # Education 
                rx.hstack(
                    rx.box(
                        rx.text("Education", font_weight="bold", color_scheme="orange", font_size="2xl"),
                        width="25%",
                        text_align="right",
                        padding_right="4",
                        margin_left="64px",
                    ),
                    rx.divider(orientation="vertical", height="auto"),
                    rx.box(
                        rx.vstack(
                            rx.heading("BSc in Data Science", size="5", margin_bottom="1"),
                            rx.text("Universidad de Buenos Aires 2022 - 2025"),
                            rx.spacer(height="4"),
                            rx.heading("BSc in Physics Science", size="5", margin_bottom="1"),
                            rx.text("Universidad de Buenos Aires 2016 - 2022"),
                            align_items="start",
                            padding="4",
                            border_radius="lg",
                            background="gray.50",
                            margin_bottom="6",
                            width="100%",
                        ),
                        width="100%",
                        margin_left="10px",

                    ),
                    align_items="flex_start",
                    margin_top="40px",
                ),
                width="100%",
            ),
            width="100%",
            max_width="1000px",
            padding_y="8",
        ),
        spacing="6",
        align="center",
        padding_y="16",
        width="100%",
        margin_bottom="100px",
    )

    
    # Projects section
    projects_section =  rx.container(
        rx.heading(
            "Data Projects",
            size="9",
            weight="medium",
            align="center",
            color_scheme="iris",
            id="projects",
            margin_bottom="20px"       
        ),
        rx.text(
            "Here are some of the projects I've worked on. Each project showcases my skills in data analysis, machine learning, and software development.",
            font_size="lg",
            align="center",
            text_align="center",
            margin_bottom="50px",
            color_scheme="yellow",
            max_width="100%",

        ),
        rx.grid(
            project_card(
                "Real-Time Purchase Propensity Prediction Using Deep Learning",
                "Built deep learning models (DeepAR, DeepTCN) to predict short-term repurchase probability based on customer time-series behaviour. ransitioned from monthly to daily pipelines to enable weekly forecasts, improving responsiveness in campaign targeting. Implemented scalable data pipelines for model training and real-time scoring.",
                ["Python", "TensorFlow", "Time Series Forecasting", "DeepAR", 'DeepTCN',' Data Pipelines', 'Real-Time Analytics', 'MLOps',' Cloud Computing'],
            ),
            project_card(
                "Customer Segmentation",
                "Created an unsupervised learning solution to identify key customer segments.",
                ["K-means", "PCA", "Pandas", "Scikit-learn"],
            ),
            project_card(
                "Predictive Modelling for Customer Behaviour in Credit and Marketing",
                "Developed machine learning models to predict weekly and monthly customer credit uptake using transactional and behavioural data. Integrated marketing campaign results and credit simulations to improve renewal predictions. Designed automated segmentation and scoring systems updated daily for real-time decision-making.",
                ["Python", "BigQuery", "Machine Learning", "Predictive Analytics", "Customer Segmentation", "Marketing Analytics"," Data Automation", "Feature Engineering"],
            ),
            columns=rx.breakpoints(
                xs="1",
                sm="1",
                md="2",
                lg="3",
                xl="3",
            ),
            spacing="9",
            width="100%",
            justify="center",
            margin_bottom="100px",
        ),
    )

    # Call to action section
    cta_section = rx.container(
        rx.box(
            rx.vstack(
                rx.heading("Ready to transform your data?", size="7", margin_bottom="4"),
                rx.text(
                    "Let's work together to extract meaningful insights from your data and drive business growth.",
                    font_size="xl",
                    margin_bottom="6",
                    max_width="800px",
                    text_align="center",
                ),
                rx.button(
                    "Get in Touch",
                    color_scheme="indigo",
                    size="4",
                    radius="large",
                    on_click=rx.redirect("/contact"),
                    padding_y="100"
                ),
                align="center",
                justify="center",
                spacing="4",
                padding_y="16",
                width="100%",
            ),
            width="100%",
            bg="indigo.500",
            color="white",
            padding="10"
        ),
        max_width="100%"
    )


    # Dark mode toggle
    dark_mode_toggle = rx.color_mode.button(
        position="fixed",
        top="0",
        left="0",
        z_index="999",
    )

    return rx.box(
        dark_mode_toggle,
        index_section,
        hero_section,
        timeline_section,
        projects_section,
        cta_section,
        width="100%",
    )