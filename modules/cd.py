from modules.library_item import LibraryItem

class Cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self, title, subject, upc)
        self.artist = artist