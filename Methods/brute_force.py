# At massive scale it is a stupid idea, don't use this shit


class BruteForce:
    def __init__(self, charset: str = '', minimum: int = 0, maximum: int = 4, *args):

        if args.__len__() <= 0 or charset.strip() == '':
            self.active = False

        self.charset = charset
        self.min = minimum
        self.max = maximum
        self.active = True
