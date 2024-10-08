from shiny import App, module, render, ui, reactive

# MODULES UI

@module.ui
def text_input_module(label, value=""):
    return ui.input_text("textInput", label, value)

@module.ui
def numeric_input_module(label):
    return ui.input_numeric("numericInput", label, 0)

@module.ui
def password_input_module(label):
    return ui.input_password("passwordInput", label)

@module.ui
def selectize_input_module(label, choices, multiple):
    return ui.input_selectize("selectizeInput", label, choices, multiple=multiple)

@module.ui
def textarea_input_module(label):
    return ui.input_text_area("textArea", label)

@module.ui
def button_module(label):
    return ui.input_action_button("actionButton", label)

# MODULES SERVEUR

#Stockage des inputs utilisateurs en attendant requêtage
userInput= {}

@module.server
def render_text_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('textInput')] = input.textInput() #update du dictionnaire

@module.server
def render_numeric_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('numericInput')] = input.numericInput()

@module.server
def render_password_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('passwordInput')] = input.passwordInput()

@module.server
def render_selectize_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('selectizeInput')] = input.selectizeInput()

@module.server
def render_textarea_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('textArea')] = input.textArea()

#Requêtage BDD
@module.server
def react_button_module(input, output, session):
    @reactive.Effect
    @reactive.event(input.actionButton)
    def _():
        if (session.ns('actionButton') == "oracle_validate-actionButton") :
            print("Search oracle DB")
            print(userInput)

        elif (session.ns('actionButton') == "postgreSQL_validate-actionButton"):
            print("Search PostGreSQL DB")

        elif (session.ns('actionButton') == "snowflake_validate-actionButton"):
            print("Search Snowflake DB")

        elif (session.ns('actionButton') == "iics_validate-actionButton"):
            print("Search IICS DB")

        elif (session.ns('actionButton') == "excel_validate-actionButton"):
            print("Search Excel file")

        else :
            print("This option doesnt exist.")