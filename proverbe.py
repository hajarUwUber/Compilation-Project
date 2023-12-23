from ply import lex

# Define the token names
tokens = ('ISM_MAWSOL', 'FI3L', '7ARF_JAR', 'ISM_MAJROR', 'HAE')

# Define the regular expressions for each token
t_ISM_MAWSOL = r'من'
t_FI3L = r'شب|شاب'
t_7ARF_JAR = r'على|علي'
t_ISM_MAJROR = r'شيء'
t_HAE = r'ه'

# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with the proverb
proverb = "من شب على شيء شاب عليه"
lexer.input(proverb)

# Print the recognized tokens
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")
