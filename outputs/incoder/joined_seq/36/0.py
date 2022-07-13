
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a plus and True otherwise.
    """
    
    sequences = re.findall(r"[A-Z]+\+[A-Z]+", text)
    
    return len(sequences) == 0 
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z")
</cell>
<cell>
joined_sequence("A+B+C+D+E+F+G+H+I+J+K+L+M+N+O