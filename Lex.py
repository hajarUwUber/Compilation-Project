from ply import lex

# Define the token names
tokens = ('ISM_MAWSOL', 'FI3L1', '7ARF_JAR1', 'ISM_MAJROR', 'HAE','FI3L2','7ARF_JAR2','MOBTADA2','KHABAR',
          '7AL','FI3L3','MAF3OL_BIH','NA2IB_DARF','ISM_MAJROR2','FA2','ADAT_CHART','FI3L4','FA3IL','FI3L5','YA2')

# Define the regular expressions for each token
t_ISM_MAWSOL = r'من'
t_FI3L1 = r'شب'
t_7ARF_JAR1 = r'على'
t_ISM_MAJROR = r'شيء'
t_HAE = r'ه'
t_FI3L2=r'شاب'
t_7ARF_JAR2=r'علي'
t_MOBTADA2=r'مراية'
t_KHABAR=r'الحب'
t_7AL=r'عمياء'
t_FI3L3=r'أعلم'
t_MAF3OL_BIH=r'الرماية'
t_NA2IB_DARF=r'كل'
t_ISM_MAJROR2=r'يوم'
t_FA2=r'ف'
t_ADAT_CHART=r'لما'
t_FI3L4=r'اشتد'
t_FA3IL=r'ساعد'
t_FI3L5=r'رمان'
t_YA2=r'ي'
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

