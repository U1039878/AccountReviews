from shiny import App, render, ui, module, Inputs, Outputs, Session
import shinyswatch
from modules.inputs import *
import pandas as pd


app_ui = ui.page_navbar(  
    ui.nav_panel("Oracle", ui.page_sidebar(  
        ui.sidebar(ui.h2(" Oracle"),
                text_input_module("oracle_hostname", "Hostname :"),
                numeric_input_module("oracle_port", "Port :"),
                text_input_module("oracle_username", "Username :"),
                password_input_module("passwordOracle", "Password :"),
                textarea_input_module("oracle_sql_query", "SQL Query :"),
                selectize_input_module("state1","Choose a state :", {}, multiple=True,),
                selectize_input_module("state2","Choose a second state :", {}, multiple=True),
                button_module("oracle_validate", "Valider"), 
                position="left", 
                bg="#f8f8f8",
                width=400),
        "Main content",) 
    ),

    ui.nav_panel("PostgreSQL", ui.page_sidebar(  
        ui.sidebar(ui.h2("PostgreSQL"),
                text_input_module("postgreSQL_hostname", "Hostname :"),
                numeric_input_module("postgreSQL_port", "Port :"),
                text_input_module("postgreSQL_username", "Username :"),
                password_input_module("postgreSQL_password", "Password :"),
                textarea_input_module("postgreSQL_sql_query", "SQL Query :"),
                selectize_input_module("state3","Choose a state :", {}, multiple=True,),
                selectize_input_module("state4","Choose a second state :", {}, multiple=True),
                button_module("postgreSQL_validate", "Valider"), 
                position="left", 
                bg="#f8f8f8",
                width=400
                ),
            "Main content",) 
    ),

    ui.nav_panel("Snowflake", ui.page_sidebar(  
        ui.sidebar(ui.h2("Snowflake")))),  

    ui.nav_panel("IICS", ui.page_sidebar(  
        ui.sidebar(ui.h2("IICS")))), 

    ui.nav_panel("Excel", ui.page_sidebar(  
        ui.sidebar(ui.h2("Excel"), 
                    ui.input_file("file_upload", "Choose Excel File", accept=[".xlsx"], multiple=False),
                    ui.output_table("table"),
                    ui.input_selectize(
                        "excel_user_header",
                        "Choose the field for user name:",
                        {},
                        multiple=False,
                    ),
                    ui.input_selectize(
                        "excel_email_header",
                        "Choose the field for email:",
                        {},
                        multiple=False,
                    ),
                    button_module("excel_validate", "Valider"), 
                    width=400, 
                ),
                ui.h3("Your excel file"),
                ui.output_data_frame("excel_input")
            )
        ),

    title="Type of technology",  
    id="page", 
    theme=shinyswatch.theme.flatly,
)  