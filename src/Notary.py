from textual import events
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea, Footer 

class main(App[str]):
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit Notary"),
        Binding("ctrl+s", "", "Save Note"),     
        Binding("ctrl+o", "focus_next", "Open Note", True)
    ]

    TITLE = "Notary"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea()
        yield Footer()
    
    def action_open(self) -> None:
        print("placeholder")
    def action_save(self) -> None:
        print("placeholder")

if __name__ == "__main__":
    app = main()
    app.run()
    
