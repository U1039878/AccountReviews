from shiny import ui
import shinyswatch
from modules.inputs import *
import pandas as pd

choices = {
    "1A": "Choice 1A", 
    "1B": "Choice 1B", 
    "1C": "Choice 1C"
}


app_ui = ui.page_navbar(  
    ui.nav_panel("Oracle", ui.page_sidebar(  
        ui.sidebar(ui.h2(" Oracle"),
                text_input_module("oracle_appication_name", "Application name"),
                text_input_module("oracle_hostname", "Hostname"),
                numeric_input_module("oracle_port", "Port"),
                text_input_module("oracle_username", "Username"),
                password_input_module("oracle_password", "Password"),
                textarea_input_module("oracle_sql_query", "SQL Query"),
                selectize_input_module("oracle_user_header", "Choose the user name field", choices),
                selectize_input_module("oracle_email_header", "Choose the field for email", choices),
                button_module("oracle_validate", "Valider"), 
                position="left", 
                bg="#f8f8f8",
                width=400),
        "Main content",) 
    ),

    ui.nav_panel("PostgreSQL", ui.page_sidebar(  
        ui.sidebar(ui.h2("PostgreSQL"),
                text_input_module("postgreSQL_appication_name", "Application name"),
                text_input_module("postgreSQL_hostname", "Hostname"),
                numeric_input_module("postgreSQL_port", "Port"),
                text_input_module("postgreSQL_username", "Username"),
                password_input_module("postgreSQL_password", "Password"),
                textarea_input_module("postgreSQL_sql_query", "SQL Query"),
                selectize_input_module("postgreSQL_user_header", "Choose the field for email", choices),
                selectize_input_module("postgreSQL_email_header", "Choose the field for email", choices),
                button_module("postgreSQL_validate", "Valider"), 
                position="left", 
                bg="#f8f8f8",
                width=400
                ),
            "Main content",) 
    ),

    ui.nav_panel("Snowflake", ui.page_sidebar(  
        ui.sidebar(ui.h2("Snowflake"),
            text_input_module("snowflake_appication_name", "Application name :"),
            text_input_module("snowflake_account_name", "Account name"),
            text_input_module("snowflake_username", "Username"), 
            password_input_module("snowflake_password", "Password"),
            text_input_module("snowflake_dbname", "Database name"),
            text_input_module("snowflake_role_name", "Role name"), 
            text_input_module("snowflake_warehouse_name", "Warehouse name"), 
            textarea_input_module("snowflake_sql_query", "SQL Query :"),
            button_module("snowflake_validate", "Valider"), 
))),  

    ui.nav_panel("IICS", ui.page_sidebar(  
        ui.sidebar(ui.h2("IICS"),
            text_input_module("iics_project_name", "Project name"),
            button_module("iics_validate", "Valider"), 
))), 

    ui.nav_panel("Excel", ui.page_sidebar(  
        ui.sidebar(ui.h2("Excel"), 
                    text_input_module("excel_appication_name", "Application name"),
                    ui.input_file("file_upload", "Choose Excel File", accept=[".xlsx"], multiple=False),
                    ui.output_table("table"),
                    selectize_input_module("excel_user_header", "Choose the field for email", choices),
                    selectize_input_module("excel_email_header", "Choose the field for email", choices),
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