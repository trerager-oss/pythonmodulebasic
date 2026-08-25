def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isuppter():
                translation = translation + "G"
            else:translat
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
