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

userInput = {} #Stockage des données en attendant requêtage

@module.server
def render_text_module(input, output, session):
    @reactive.effect
    def _():
        userInput[session.ns('textInput')] = input.textInput() #update du dictionnaire
        print(userInput)

@module.server
def render_numeric_module(input, output, session):
    @reactive.effect
    def _():
        print(input.numericInput())

@module.server
def render_password_module(input, output, session):
    @reactive.effect
    def _():
        print(input.passwordInput())

@module.server
def render_selectize_module(input, output, session):
    @reactive.effect
    def _():
        print(input.selectizeInput())

@module.server
def render_textarea_module(input, output, session):
    @reactive.effect
    def _():
        print(input.textArea())

