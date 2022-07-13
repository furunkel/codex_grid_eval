
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with an underscore and False otherwise.
    """
    return bool(re.search(r'[A-Z]+_[A-Z]+', text))

def main():
    print(joined_sequence('A_B_C'))
    print(joined_sequence('A_B_C_'))
    print(joined_sequence('A_B_C_D'))
    print(joined_sequence('A_B_C_D_'))
    print(joined_sequence('A_B_C_D_E'))
    print(joined_sequence('A_B_C_D_E_'))
    print(joined_sequence('A_B_C_D_E_F'))
    print(joined_sequence('A_B_C_D_E_F_'))
    print(joined_sequence('A_B_C_D_E_F_G'))
    print(joined_sequence('A_B_C_D_E_F_G_'))
    print(joined_sequence('A_B_C_D_E_F_G_H'))
    print(joined_sequence('A_B_C_D_E_F_G_H_'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_