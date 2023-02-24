from Code.display import Display

class Director:
    def __init__(self):
        self.display = Display()
        self.user = ""
        self.keep_going = True
        

    def start(self):
        self.display.get_user_name()

    

    
# TODO research selenium to web scrape data from websites