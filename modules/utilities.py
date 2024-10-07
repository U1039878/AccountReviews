from shiny import App, module, render, ui
import shinyswatch

@module.ui
def radioButtonUI(id):
  ns <- NS(id)
  uiOutput(ns("radioButton"))
}

radioButtonServer <-
  function(id,
           inputLabel,
           inputChoices,
           inputSelected) {
    moduleServer(id,
                 function(input, output, session) {
                   output$radioButton <- renderUI({
                     ns <- session$ns
                     radioButtons(
                       ns("rb")
                       ,
                       label = inputLabel,
                       choices = inputChoices,
                       inline = TRUE,
                       selected = inputSelected
                     )
                   })
                 })
  }

app_ui = ui.page_fluid(
    ui.input_radio_buttons(  
        "radio",  
        "Radio buttons",  
        {"1": "Option 1", "2": "Option 2", "3": "Option 3"},  
    ),  
    ui.output_ui("value"),
)

def server(input, output, session):
    @render.ui
    def value():
        return input.radio()

app = App(app_ui, server)