text = 'олоол ололл оллоо гшщ фбв абвав абв'
deleted_symbols = 'абв'

for i in text.split():
    if deleted_symbols in i:
        text = text.replace(i, '')

print(text)