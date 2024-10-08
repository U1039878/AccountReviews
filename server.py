from shiny import App, module, render, ui, reactive
from modules.inputs import *
import pandas as pd




def app_server(input, output, session):
    #Oracle panel
    render_text_module("oracle_appication_name")
    render_text_module("oracle_hostname")
    render_numeric_module("oracle_port")
    render_text_module("oracle_username")
    render_password_module("passwordOracle")
    render_textarea_module("oracle_sql_query")
    render_selectize_module("oracle_user_header")
    react_button_module("oracle_validate")



    #PostgreSQL panel
    render_text_module("postgreSQL_appication_name")
    render_text_module("postgreSQL_hostname")
    render_numeric_module("postgreSQL_port")
    render_text_module("postgreSQL_username")
    render_password_module("postgreSQL_password")
    render_textarea_module("postgreSQL_sql_query")
    react_button_module("postgreSQL_validate")

    #Snowflake panel
    render_text_module("snowflake_appication_name")
    render_text_module("snowflake_account_name")
    render_text_module("snowflake_username")
    render_password_module("snowflake_password")
    render_text_module("snowflake_dbname")
    render_text_module("snowflake_role_name")
    render_text_module("snowflake_warehouse_name")
    render_textarea_module("snowflake_sql_query")
    react_button_module("snowflake_validate")

    #IICS panel
    render_text_module("iics_project_name")
    react_button_module("iics_validate")


    #EXCEL PANEL
    render_text_module("excel_appication_name")
    render_selectize_module("excel_user_header")
    render_selectize_module("excel_email_header")



    @render.data_frame  
    def excel_input():
        # Vérifie si un fichier a été téléchargé
        if input.file_upload() is not None:
            # Lire le fichier Excel en dataframe avec pandas
            file_info = input.file_upload()[0]  # Récupère les infos du fichier
            df = pd.read_excel(file_info["datapath"])  # Lit le fichier Excel
            comlumnNames = df.columns
            listColumnNames = comlumnNames.tolist()
            ui.update_selectize("excel_user_header-selectizeInput", choices=listColumnNames)
            ui.update_selectize("excel_email_header-selectizeInput", choices=listColumnNames)


            # Retourner le dataframe pour l'afficher dans l'UI
            return df
        else:
            print("No file found")
            return pd.DataFrame() # Retourner un dataframe vide si aucun fichier n'est chargé
    
    react_button_module("excel_validate")

