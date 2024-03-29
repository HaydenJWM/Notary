from textual.widgets import Input
from textual.screen import ModalScreen
from textual.app import ComposeResult


class SaveScreen(ModalScreen):
    
    def compose(self) -> ComposeResult:
        yield Input(placeholder = "Filename:") 
