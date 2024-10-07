from shiny import App, module, render, ui, reactive
from modules.inputs import *
import pandas as pd




def app_server(input, output, session):
    #Oracle panel
    render_text_module("oracle_hostname")
    render_numeric_module("oracle_port")
    render_text_module("oracle_username")
    render_password_module("passwordOracle")
    render_textarea_module("oracle_sql_query")
    render_selectize_module("state1")
    render_selectize_module("state2")
    react_button_module("oracle_validate")



    #PostgreSQL panel
    render_text_module("postgreSQL_hostname")
    render_numeric_module("postgreSQL_port")
    render_text_module("postgreSQL_username")
    render_password_module("postgreSQL_password")
    render_textarea_module("postgreSQL_sql_query")
    render_selectize_module("state3")
    render_selectize_module("state4")
    react_button_module("postgreSQL_validate")

    #Snowflake panel
    react_button_module("snowflake_validate")

    #IICS panel
    react_button_module("iics_validate")


    #EXCEL PANEL
    
    @render.data_frame  
    def excel_input():
        # Vérifie si un fichier a été téléchargé
        if input.file_upload() is not None:
            # Lire le fichier Excel en dataframe avec pandas
            file_info = input.file_upload()[0]  # Récupère les infos du fichier
            df = pd.read_excel(file_info["datapath"])  # Lit le fichier Excel
            comlumnNames = df.columns
            listColumnNames = comlumnNames.tolist()
            ui.update_selectize("excel_user_header", choices=listColumnNames)
            ui.update_selectize("excel_email_header", choices=listColumnNames)

            # Retourner le dataframe pour l'afficher dans l'UI
            return df
        else:
            print("No file found")
            return pd.DataFrame() # Retourner un dataframe vide si aucun fichier n'est chargé
    
    react_button_module("excel_validate")

    
