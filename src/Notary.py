import sys
from textual import events
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea, Footer 

class main(App[str]):
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit Notary"),
        Binding("ctrl+s", "save()", "Save Note"),     
        Binding("ctrl+o", "open()", "Open Note")
    ]

    TITLE = "Notary"
   
    noteArea = None

    def compose(self) -> ComposeResult:
        self.noteArea = TextArea()
        yield Header()
        yield self.noteArea
        yield Footer()
    
    def action_open(self) -> None:
        print("placeholder")
    
    def action_save(self) -> None:
        f = open("HelloWorld.txt", "x")
        f.write(self.noteArea.text)
        f.close()

if __name__ == "__main__":
    filename = ""

    #If a filename was given in the command line then open it
    if(len(sys.argv) >= 2):
        filename = sys.argv[1]
        
    app = main()
    app.run()
    
