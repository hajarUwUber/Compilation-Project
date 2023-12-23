from ply import lex

# Define the token names
tokens = ('MOBTADAE1', 'MOBTADAE2', 'khabar12', 'DARFZAMAN', 'FI3L1', 'FA3IL1', 'FI3L2', 'FA3IL2', 'MOBTADAE3', 'HARFJAR', 'ISMMAJROR', 'KAAF','MODAFILAYH','HAAE')

# Define the regular expressions for each token
t_MOBTADAE1 = r'الصبر'
t_MOBTADAE2 = r'مفتاح'
t_khabar12 = r'الفرج'
t_DARFZAMAN = r'اذا'
t_FI3L1 = r'تم'
t_FA3IL1 = r'العقل'
t_FI3L2 = r'نقص'
t_FA3IL2= r'الكلام'
t_MOBTADAE3= r'الدال'
t_HARFJAR = r'على'
t_ISMMAJROR = r'الخير'
t_KAAF = r'ك'
t_MODAFILAYH = r'فاعل'
t_HAAE = r'ه'

# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with the proverbs
proverb1 = "الصبر مفتاح الفرج"
proverb2 = "اذا تم العقل نقص الكلام"
proverb3 = "الدال على الخير كفاعله"

# Tokenize and print the recognized tokens for the first proverb
lexer.input(proverb1)
print("Tokens for proverb1:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

# Tokenize and print the recognized tokens for the second proverb
lexer.input(proverb2)
print("\nTokens for proverb2:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

# Tokenize and print the recognized tokens for the third proverb
lexer.input(proverb3)
print("\nTokens for proverb3:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")
