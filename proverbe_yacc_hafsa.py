from ply import lex

# Define the token names
tokens = (
    'MOBTADAE1', 'MOBTADAE2', 'MODAF', 'KHABAR1', 'KHABAR2', 'ISM1', 'ISM2', 'FI3L1', 'FI3L2', 'MAF3OULBIH', 'HAL',
    'HARF1', 'HARF2', 'HARF3', 'DAMIR'
)

# Define the regular expressions for each token
t_MOBTADAE1 = r'حبل'
t_MOBTADAE2 = r'الدهر'
t_MODAF = r'الكذب'
t_KHABAR1 = r'قصير'
t_KHABAR2 = r'يومان'
t_ISM1 = r'يوم'
t_ISM2 = r'من'
t_MAF3OULBIH = r'الناس'
t_FI3L1 = r'راقب'
t_FI3L2 = r'مات'
t_HAL = r'همًا'
t_HARF1 = r'ل'
t_HARF2 = r'و'
t_HARF3 = r'علي'
t_DAMIR = r'ك'

# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with the proverbs
proverb1 = "حبل الكذب قصير"
proverb2 = "من راقب الناس مات همًا"
proverb3 = "الدهر يومان يوم لك ويوم عليك"

lexer.input(proverb1)
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

# Reset lexer position
lexer.lineno = 1

lexer.input(proverb2)
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

lexer.lineno = 1

lexer.input(proverb3)
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")
