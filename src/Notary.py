import sys
from textual import events
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea, Footer 

class Notary(App[str]):
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit Notary"),
        Binding("ctrl+s", "save()", "Save Note"),     
        Binding("ctrl+o", "open()", "Open Note")
    ]
    TITLE = "Notary"
    noteArea = None
    filename = None

    def initFilename(self):
        #If filename was given in the args use it
        if(len(sys.argv) >= 2):
            self.filename = sys.argv[1]


    def compose(self) -> ComposeResult:
        self.noteArea = TextArea()
        self.initFilename()

        yield Header()
        yield self.noteArea
        yield Footer()

    def action_open(self) -> None:
        print("placeholder")
    
    def action_save(self) -> None:
        f = open(self.filename, "x")
        f.write(self.noteArea.text)
        f.close()

if __name__ == "__main__": 
    app = Notary()
    app.run()
    
