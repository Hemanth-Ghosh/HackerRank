import re
for _ in range(int(input())):
    card = input()
    val=0
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$',card) and \
       not re.search(r'(\d)\1{3,}',''.join(card.split('-'))):
       val=1        
    if val:
        print("Valid")
    else:
        print("Invalid")
