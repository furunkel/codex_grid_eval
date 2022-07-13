
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a plus and True otherwise.
    """
    
    letters = re.findall(r'[a-z]+', text)
    
    if len(letters) != 0:
        
        joined = letters[0]
        
        for letter in letters[1:]:
            
            if letter.isupper():
                
                joined += '+' + letter
                
            else:
                
                joined += letter
                
        return joined.isupper()
    
    else:
        
        return False
    
    
#Test Cases
print(joined_sequence(''))
print(joined_sequence('abc'))
print(joined_sequence('abC'))
print(joined_sequence('abCd'))
print(joined_sequence('abCdE'))
print(joined_sequence('abCdEf'))
print(joined_sequence('abCdEfG'))
print(joined_sequence('abCdEfGh'))
print(joined_sequence('abCdEfGhi'))
print(joined_sequence('abCdEfGhij'))
print(joined_sequence('abCdEfGhijK'))
print(joined_sequence('abCdEfGhijKl'))
print(joined_sequence('abCdEfGhijKlM'))
print(joined_sequence('abCdEfGhijKlMN'))
print(joined_sequence('abCdEfGhijKlMNO'))
print(joined_sequence('abCdEfGhijKlMNOP'))
print(joined_sequence('abCdEfGhijKlMNOPQ'))
print(joined_sequence('abCdEfGhijKlMNOPQR'))
print(joined_sequence('abCdEfGhijKlMNOPQRS'))
print(joined_sequence('abCdEfGhijKlMNOPQRST'))
print(joined_sequence('abCdEfGhijKlMNOPQRSTU'))
print(joined_sequence('abCdEfGhijKlMNOPQRSTUV'))
print(joined_sequence('abCdEfGhijKlMNOPQRSTUVW'))
print(joined_sequence('abCdEfGhijKlMNOPQRSTUVWV'))
print(joined_sequence('abCdEfGhijKlM