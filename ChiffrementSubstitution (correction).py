# ================ A REMPLIR ========================================
ALPHABET = {
    "A":"K",
    "B":"L",
    "C":"R",
    "D":"O",
    "E":"B",
    "F":"G",
    "G":"U",
    "H":"A",
    "I":"Y",
    "J":"M",
    "K":"S",
    "L":"P",
    "M":"C",
    "N":"F",
    "O":"Z",
    "P":"X",
    "Q":"V",
    "R":"N",
    "S":"T",
    "T":"D",
    "U":"I",
    "V":"J",
    "W":"H",
    "X":"Q",
    "Y":"W",
    "Z":"E",
}

#==================================


MESSAGE = "Comme Leclerc entra aux Invalides, avec son cortege d'exaltation dans le soleil d'Afrique, entre ici, Jean Moulin, avec ton terrible cortege. Avec ceux qui sont morts dans les caves sans avoir parle, comme toi, et meme, ce qui est peut-etre plus atroce, en ayant parle. Andre MALRAUX"

def main():
    msg: str = MESSAGE.upper()
    alphabet = ALPHABET
    print(f"Le message: {msg}")
    print(f"============\n{chiffrement(msg, alphabet)}")

def chiffrement(msg, alpha):
    output: str = ""
    for lettre in msg:
        if lettre == ' ' or lettre == '.' or lettre == ',' or lettre =="'" or lettre=='-':
            output += lettre
        else:
            output += alpha[lettre]
    return output

main()