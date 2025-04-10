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
                spacing="5",
                justify="end",
                margin_top="40px",
                margin_right="40px",
            )

    hero_section = rx.container(
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
                "I build data-driven solutions that solve real-world problems and drive business impact.",
                font_size="lg",
                text_align="left",
                margin_bottom="8",
            ),
            rx.text(
                "I'm a Data Scientist with 7 years of experience turning data into actionable insights."
                "My background combines a strong foundation in statistics, machine learning, and data engineering, with a deep interest in solving business problems."
                "I've worked on credit scoring models, customer segmentation, predictive analytics, and real-time dashboards."  
                "I enjoy transforming complex datasets into clear, meaningful results that support strategic decisions."
                "Currently, I’m focused on building scalable data products, improving model performance, and bridging the gap between technical and business teams.",
                font_size="lg",
                text_align="left",
                margin_bottom="8",
            ),
            spacing="6",
            justify="center",
            align="start",
            padding_y="16",
            min_height="85vh",
        ),
        max_width="1200px",
    )

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
            text_align="center",
            margin_bottom="50px",
            color_scheme="yellow"
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
            margin_bottom="100px"
        )
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
        projects_section,
        cta_section,
        width="100%",
    )