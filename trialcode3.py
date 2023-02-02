class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


CardArray = [0 for i in range(30)]
#
# try:
#     Filename = "CardValues.txt"
#     File = open(Filename, 'r')
#     for x in range(30):
#         NumberRead = int(File.readline())
#         ColourRead = File.readline()
#         print(NumberRead)
#         print(ColourRead)
#         CardArray[x] = Card(NumberRead, ColourRead)
#     File.close()
# except IOError:
#     print("Could not find your file named", Filename)

CardFile = open("CardValues.txt", 'r')

for Count, Value in enumerate(CardArray):
    CardArray[Count]=CardFile.readline[Count]

CardFile.close()
print(CardArray)
