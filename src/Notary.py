from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Header, TextArea, Footer 

class main(App[str]):
    TITLE = "Notary"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea()
        yield Footer()

    


if __name__ == "__main__":
    app = main()
    app.run()
    
