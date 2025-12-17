from converter import Converter

converter = Converter()

raw_input = input("Enter the text to convert into Morse Code:\n")

morse_code = converter.convert(raw_input)

print("The morse code for " + raw_input + " is:\n" + morse_code)