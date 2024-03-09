from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Header, RichLog

class main(App[str]):
    TITLE = "Notary"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(RichLog).write(event)


if __name__ == "__main__":
    app = main()
    app.run()
    
