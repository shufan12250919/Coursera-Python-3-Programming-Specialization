VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt): 
        """Add amt to self.prizeMoney"""
        self.prizeMoney += amt

    def goBankrupt(self): 
        """Set self.prizeMoney to 0"""
        self.prizeMoney = 0

    def addPrize(self, prize): 
        """Append prize to self.prizes"""
        self.prizes.append(prize)

    def __str__(self): 
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        prompt = """{} has ${}
Category: {}
Phrase:  {}
Guessed: {}

Guess a letter, phrase, or type 'exit' or 'pass':""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed)
    
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        coint = random.randint(1, 10)
        if coint > self.difficulty:
            return True
        else:
            return False
 
    def getPossibleLetters(self, guessed):
        lst = []
        for c in LETTERS:
            if c in VOWELS and self.prizeMoney < VOWEL_COST:
                continue
            if c not in guessed:
                lst.append(c)
        return lst
    
    def getMove(self, category, obscuredPhrase, guessed):
        guess = self.getPossibleLetters(guessed)
        if len(guess) == 0:
            return 'pass'
        if(self.smartCoinFlip()):
            for c in self.SORTED_FREQUENCIES:
                if c in guess:
                    return c
        else:
            return random.choice(guess)
