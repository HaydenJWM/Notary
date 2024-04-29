import sys
from pathlib import Path
from textual import events, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea, Footer, Input 
from textual.screen import Screen, ModalScreen
from SaveScreen import SaveScreen
from OpenScreen import OpenScreen

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
        self.action_open()

    #Textual based function that acts as a constructor of sorts
    def compose(self) -> ComposeResult:
        self.noteArea = TextArea()
        self.processArguments(sys.argv)

        yield Header()
        yield self.noteArea
        yield Footer()

    #Opens a file for writing
    @work
    async def action_open(self) -> None:
        #Open screen to get filename here
        if(self.filename == None):
            self.filename = await self.push_screen_wait(OpenScreen())

        if(Path("data/"+self.filename).exists()):
            f = Path("data/"+self.filename).open("r")
            fileContents = f.read()
            if(len(fileContents) != 0):
                self.noteArea.text = fileContents

    #Saves the current file contents
    @work
    async def action_save(self) -> None:
        fileOp = "w"
        #If filename was not given in the CLI, get a filename from the TUI
        if(self.filename == None):
            self.filename = await self.push_screen_wait(SaveScreen())
        f = Path("data/"+self.filename).open(fileOp)
        f.write(self.noteArea.text)
        f.close()

if __name__ == "__main__": 
    app = Notary()
    app.run()
    
