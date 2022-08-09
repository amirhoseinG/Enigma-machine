
class Enigma():

    def __init__(self, plain):

        self.rotorsOne = "zkaytgvnqwcdseupxjhlfomirb".upper()
        self.rotorsSecond = "wensuhkiopcfrgvzdltyxamqbj".upper()
        self.rotorsThird = "gkcybnhefdprzwxoiumjavltqs".upper()
        self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
        self.cipher = ""

        self.plain = plain.upper()
        self.numberRotations = 0

    def cipherRes(self):

        for char in self.plain:
            if char == " ":
                self.cipher += " "
                self.numberRotations += 1
                self.rotations()
            else:
                self.numberRotations += 1
                self.cipher += self.enigmaMain(char)
                self.rotations()
            
        return self.cipher.lower()

    def enigmaMain(self, char):

        code = self.rotorsOne[self.alpha.find(char)]
        codeSecond = self.rotorsSecond[self.alpha.find(code)]
        codeThird = self.rotorsThird[self.alpha.find(codeSecond)]
        reflect = self.Reflactor(codeThird)
        codeThird = self.alpha[self.rotorsThird.find(reflect)]
        codeSecond = self.alpha[self.rotorsSecond.find(codeThird)]
        code = self.alpha[self.rotorsOne.find(codeSecond)]

        return code

    def rotations (self):

        self.rotorsOne = self.rotorsOne[1:] + self.rotorsOne[0]
        if self.numberRotations % 26 == 0:
            self.rotorsSecond = self.rotorsSecond[1:] + self.rotorsSecond[0]
        if self.numberRotations % 26*26 == 0:
            self.rotorsThird = self.rotorsThird[1:] + self.rotorsThird[0]

    def Reflactor(self, code):

        return self.alpha[len(self.alpha) - self.alpha.find(code) - 1]





if __name__ == "__main__":

    text = input("Please enter : ")
    plain = Enigma(text)
    print(plain.cipherRes())
