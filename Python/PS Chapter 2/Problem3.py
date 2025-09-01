name = input("Enter your name: ")
date = input("Enter date: ")

letter = ''' Dear <|Name|>
             You are selected
             <|Date|>'''

print(letter.replace("<|Name|>",name).replace("<|Date|>",date).strip)