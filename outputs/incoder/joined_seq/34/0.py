
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a minus and True otherwise.
    """
    
    sequences = re.findall(r'[A-Z]+[a-z]+', text)
    
    if len(sequences) > 0:
        
        joined = sequences[0]
        
        for sequence in sequences:
            
            if sequence.isupper():
                
                joined = joined + sequence
                
            else:
                
                if joined.isupper():
                    
                    joined = joined + '-'
                    
                else:
                    
                    return False
                
        return True
    
    else:
        
        return False
    
    
# Test Cases
print(joined_sequence("AaBbCc"))
print(joined_sequence("AaBbCcDdEe"))
print(joined_sequence("AaBbCcDdEeFf"))
print(joined_sequence("AaBbCcDdEeFfGg"))
print(joined_sequence("AaBbCcDdEeFfGgHh"))
print(joined_sequence("AaBbCcDdEeFfGgHhIi"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbCcDdEeFfGgHhIj"))
print(joined_sequence("AaBbC