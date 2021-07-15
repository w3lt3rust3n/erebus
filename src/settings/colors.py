class Colors:
    """gn"""
    def __init__(self):
        self.red   = "\033[1;31m"
        self.blue  = "\033[1;34m"
        self.cyan  = "\033[1;36m"
        self.green = "\033[0;32m"
        self.reset = "\033[0;0m"
        self.bold    = "\033[;1m"
        self.reverse = "\033[;7m"

    def pprint(self, color,string=None, attr_color=None):
        if color == "red":
            return print(self.red + "{}".format(string))
        if color == "blue":
            return print(self.blue + "{}".format(string))
        if color == "cyan":
            return print(self.cyan + "{}".format(string))
        if color == "green":
            return print(self.green + "{}".format(string))
        if color == "reset":
            return print(self.reset + "{}".format(string))
        if color == "bold":
            return print(self.bold + "{}".format(string))
        if color == "reverse":
            return print(self.reverse + "{}".format(string))

