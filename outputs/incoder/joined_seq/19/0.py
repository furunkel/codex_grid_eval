
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.
    """
    
    sequences = re.findall("[a-z]{6}__[a-z]{6}", text)
    
    if len(sequences) > 0:
        return True
    else:
        return False
</cell>
<cell>
joined_sequence("a__b_c__d_e__f__g__h")
</cell>
<cell>
joined_sequence("a__b_c__d_e__f__g__h__i__j__k__l__m__n__o__p__q__r__s__t__u__v__w__x__y__z")
</cell>
<text>
Question 7
Write a function that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.


</text>
<cell>
def joined_sequence_2(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.
    """
    
    sequences = re.findall("[a-z]{6}__[a-z]{6}", text)
    
    if len(sequences) > 0:
        return True
    else:
        return False
</cell>
<cell>
joined_sequence_2("a__b_c__d_e__f__g__h")
</cell>
<cell>
joined_sequence_2("a__b_c__d_e__f__g__h__i__j__k__l__m__n__o__p__q__r__s__t__u__v__w__x__y__z")
</cell>
<text>
Question 8
Write a function that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.


</text>
<cell>
def joined_sequence_3(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.
    """
    
    sequences = re.findall("[a-z]{6}__[a-z]{6}", text)
    
    if len(sequences) > 0:
        return True
    else:
        return False
</cell>
<cell>
joined_sequence_3("a__b_c__d_e__f__g__h")
</cell>
<cell>
joined_sequence_3("a__b_c__d_e__f__g__h__i__j__k__l__m__n__o__p__q__r__s__t__u__v__w__x__