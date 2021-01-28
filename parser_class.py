class Parser:
    def __init__(self, parse_file):
        self.lines = open(parse_file, "r").readlines()
        self.characters = open(parse_file, "r").read()

    def parser_func(self):
        """ Assigning variables to the constructor """
        total_sentences = len(self.lines)
        total_characters = len(self.characters)

        return {"sentences": [total_sentences],
                "stats": {"total_sentences": total_sentences, "total_characters": total_characters}}
