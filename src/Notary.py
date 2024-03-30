import sys
from textual import events, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea, Footer, Input 
from textual.screen import Screen, ModalScreen
from SaveScreen import SaveScreen

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

    #Opens a file for writing
    def action_open(self) -> None:
        print("placeholder")
   
    #Saves the current file contents            
    #TODO: Check if file has been modified and save only if something has changed
    @work
    async def action_save(self) -> None:
        fileOp = "w"
        #If filename was not given in the CLI, get a filename from the TUI
        if(self.filename == None):
            self.filename = await self.push_screen_wait(SaveScreen())
        f = open(self.filename, fileOp)
        f.write(self.noteArea.text)
        f.close()

if __name__ == "__main__": 
    app = Notary()
    app.run()
    
