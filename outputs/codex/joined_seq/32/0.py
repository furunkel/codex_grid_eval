
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with six underscores and True otherwise.
    """
    return re.search(r'[A-Z]{2,}_+[A-Z]{2,}', text) is None

def main():
    """
    Test your functions by running:

        python regex.py
    """
    assert contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")
    assert contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")
    assert contains_acronym("Please do NOT enter without permission!")
    assert contains_acronym("PostScript is a fourth-generation programming language (4GL)")
    assert not contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)")

    assert long_repeat('sdsffffse') == 4
    assert long_repeat('ddvvrwwwrggg') == 3

    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True

    assert is_acceptable_password('aaaaaaaaaaaaaaaaaaaaa') == False
    assert is_acceptable_password('aaaaaaaaaaaaaaaaaaaaaa') == True

    assert from_dictionary(["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]) == "below"
    assert from_dictionary(["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]) == "down"
    assert from_dictionary(["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]) == "how"
    assert from_dictionary(["below","down","go","going","horn","how","howdy","it","i","low