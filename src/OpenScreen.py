from textual import on
from textual.widgets import Input, Button
from textual.screen import Screen
from textual.app import ComposeResult, App

#TODO: Add file extension validation
class OpenScreen(Screen[str]):
   
    filenameInput = None

    def compose(self) -> ComposeResult:
        self.filenameInput = Input(placeholder="Filename:")
        yield self.filenameInput
        yield Button("Open", id="open")

    @on(Button.Pressed, "#open")
    def handle_save(self) -> None:
        if(self.filenameInput.value != None):
            self.dismiss(self.filenameInput.value)
