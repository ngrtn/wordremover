def reset():
    rest = str(input('Do you want to start again? y/n\n'))
    if rest == 'y':
        main()
    if rest == 'n':
        print()

def main(): # main code
    print('Welcome to Word Remover!\nTo start paste your text below') # \n used as new line
    sentence = str(input()) # getting phrase
    print('You typed:', sentence)
    print('if you made a mistake type "Cancel"\nOr type "Next"')

    checking1 = str(input()) # checking if user made a mistake at sentence (level 2)
    if checking1 == "Cancel":
        main() # reset to the start
    if checking1 == "Next": # continue
        toremove = str(input('Please enter word/words to remove: ')) # getting words to remove (level 3)
        result = sentence.replace(toremove, "")
        print('Result:', result)
        reset()
main() # starting Code (yeah, at the end)