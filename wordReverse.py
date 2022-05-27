#! python3
#! Reverse the words in the sentence  without reversing the order of the words in the sentence.

sent = "The quick brown fox jumped over the dog"
revSent = "ehT kciuq nworb xof depmuj revo eht god"


def example():
    return revSent


def answer():
    return " ".join(sent[::-1].split()[::-1])


print(answer())
if answer() == revSent:
    print("That's correct!")
else:
    print("That is incorrect, try again.")
