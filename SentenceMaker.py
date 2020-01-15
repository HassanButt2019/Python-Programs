def Sentence_Maker(phreses):
    Interrogative = ("Is" , "Are" ,"Was","Did", "Does", "What" , "What's", "Where" ,"How" ,"Do" ,"When")
    Interrogative_Small = ("is", "are", "was", "did", "does", "what", "what's", "where", "how", "do", "when")
    Capitalized = phreses.capitalize()
    if phreses.startswith(Interrogative) or phreses.startswith(Interrogative_Small):
        return "{}?".format(Capitalized)
    else:
        return "{}.".format(Capitalized)


Userinput = " "
result = []
while True:
    Userinput = input("Say SomeThing : ")

    if Userinput == "\end":
        break
    else:
        result.append(Sentence_Maker(Userinput))



print(" ".join(result))