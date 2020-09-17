'''def m1(input):
    word = input.split(" ")
    word= word[-1::-1]
    output = ' '.join(word)
    return output
if __name__ == "__main__":
    input = 'what is your name'
    print(m1(input))'''




def reverseword(input):
    inputwords=input.split(" ")
    inputwords=inputwords[-1::-1]
    output=' '.join(inputwords)
    print(output)
reverseword(" biswa ranjan roul")

