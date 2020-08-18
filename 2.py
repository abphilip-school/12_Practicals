class myclass:
    def charCount(string):
        return len(string)
    def capitalize(string):
        return string.capitalize()
    def letter(char):
        if char.isdigit() == True:
            return "Number"
        elif char.isalpha() == True:
            return "Letter"
        else:
            return "Special Character"
    def toUpper(string):
        return string.upper()

    strin = raw_input("Enter the string: ")
    l = charCount(strin)
    s = capitalize(strin)
    ch = s[0]
    type_of_ch = letter(ch)
    conv = toUpper(strin)

    print "Length:",l
    print "Capitalize: ",s
    print "Type:",type_of_ch
    print "Upper Case:",conv

