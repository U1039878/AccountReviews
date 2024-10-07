from shiny import App, module, render, ui
from ui import app_ui
from server import app_server

app = App(app_ui, app_server)
