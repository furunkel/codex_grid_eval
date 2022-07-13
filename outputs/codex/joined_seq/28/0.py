
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with an underscore and True otherwise.
    """
    return re.search(r'[A-Z]_[A-Z]', text) is None

def main():
    print(joined_sequence('A_B'))
    print(joined_sequence('A_b'))
    print(joined_sequence('A_B_C'))
    print(joined_sequence('A_B_C_D'))
    print(joined_sequence('A_B_C_D_E'))
    print(joined_sequence('A_B_C_D_E_F'))
    print(joined_sequence('A_B_C_D_E_F_G'))
    print(joined_sequence('A_B_C_D_E_F_G_H'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L_M'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L_M_N'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L_M_N_O'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P'))
    print(joined_sequence('A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q'))
    print(joined_sequence('A_B_C_D_E_F_G