class Converter:
    def import_code(self):
        """Import the text file with the conversions and add them to the dictionary"""
        with open("code.txt") as f:
            for x in f:
                line = x.split(" ")
                line[1] = line[1].strip()
                self.code[str(line[0])] = line[1]

    def __init__(self):
        """Set up the variables"""
        self.code = {}
        self.import_code()
        self.letter_gap = "   "
        self.word_gap = "       "

    def convert(self, raw_input):
        """Take the raw input, loop through each character and convert to imported code"""
        split_input = raw_input.upper()
        return_message = ""
        for letter in split_input:
            if letter in self.code:
                return_message = return_message + self.code[letter] + self.letter_gap
            else:
                return_message = return_message + self.word_gap
        return return_message
