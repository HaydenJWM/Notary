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

    #Process command line arguments into variables/flags
    #Current argument structure:
    #   0: Program Name
    #   1: Filename to open/save to
    def processArguments(self, args):
        if(len(args) <= 1):
            return
        
        self.filename = args[1]

    #Textual based function that acts as a constructor of sorts
    def compose(self) -> ComposeResult:
        self.noteArea = TextArea()
        self.processArguments(sys.argv)

        yield Header()
        yield self.noteArea
        yield Footer()

    def action_open(self) -> None:
        print("placeholder")
   
    #Saves the current message contents
    #NOTE: Currently requires a filename input from the CLI
    #TODO: If filename is none type open an input widget and take a filename to use            
    def action_save(self) -> None:
        if(self.filename == None):
            return
        f = open(self.filename, "x")
        f.write(self.noteArea.text)
        f.close()

if __name__ == "__main__": 
    app = Notary()
    app.run()
    
