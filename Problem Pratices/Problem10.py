letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>","07 july 2006"))