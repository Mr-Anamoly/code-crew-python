#Caesar shift Cipher lets try this program using python'


print(f"############## Cracking Caesar Shift Cipher Program ##############\n")
print(f"(one word at a time)\n") 

code=list(input("Enter the code to decrypt: "))
print(f"\nCode to decrypt: {code}\n")

listletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
listletters2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# All-bmm
n=0


while n<27 :
    decrypted = ""
    for char in code:
        try:
            var = listletters.index(char)
        except ValueError:
            var = listletters2.index(char)
        shiftvar = var - n
        decrypted = decrypted + listletters[shiftvar]
    
    print(f"Shift {n}: {decrypted}")
    input("Press enter to continue...")
    n+=1

# The logic took me half an hour to figure out but I finally did it from zero.
# quite bad but need improvements.
