from textual import on
from textual.widgets import Input,Button
from textual.screen import Screen
from textual.app import ComposeResult, App

#TODO: Add file extension validation. Add CSS. Add Header/Footer
class SaveScreen(Screen[str]):
 
    filenameInput = None

    def compose(self) -> ComposeResult:
        self.filenameInput = Input(placeholder = "Filename:")
        yield self.filenameInput
        yield Button("Save", id="save")

    @on(Button.Pressed, "#save")
    def handle_save(self) -> None:
        self.dismiss(self.filenameInput.value)

