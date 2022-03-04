# ================ A REMPLIR ========================================
ALPHABET = {
    " ":"A",
    " ":"B",
    " ":"C",
    " ":"D",
    " ":"E",
    " ":"F",
    " ":"G",
    " ":"H",
    " ":"I",
    " ":"J",
    " ":"K",
    " ":"L",
    " ":"M",
    " ":"N",
    " ":"O",
    " ":"P",
    " ":"Q",
    " ":"R",
    " ":"S",
    " ":"T",
    " ":"U",
    " ":"V",
    " ":"W",
    " ":"X",
    " ":"Y",
    " ":"Z",
}

#==================================


MESSAGE = "RZCCB PBRPBNR BFDNK KIQ YFJKPYOBT, KJBR TZF RZNDBUB O'BQKPDKDYZF OKFT PB TZPBYP O'KGNYVIB, BFDNB YRY, MBKF CZIPYF, KJBR DZF DBNNYLPB RZNDBUB. KJBR RBIQ VIY TZFD CZNDT OKFT PBT RKJBT TKFT KJZYN XKNPB, RZCCB DZY, BD CBCB, RB VIY BTD XBID-BDNB XPIT KDNZRB, BF KWKFD XKNPB."

def main():
    msg: str = MESSAGE
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