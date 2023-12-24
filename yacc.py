from ply import lex, yacc
from proverbe import tokens
# tokens = ('ISM_MAWSOL', 'FI3L1', '7ARF_JAR1', 'ISM_MAJROR', 'HAE','FI3L2','7ARF_JAR2')

# # Define the regular expressions for each token
# t_ISM_MAWSOL = r'من'
# t_FI3L1 = r'شب'
# t_7ARF_JAR1 = r'على'
# t_ISM_MAJROR = r'شيء'
# t_HAE = r'ه'
# t_FI3L2=r'شاب'
# t_7ARF_JAR2=r'علي'
# # Ignore whitespace
# t_ignore = ' \t\n'

# # Error handling rule
# def t_error(t):
#     print(f"Illegal character: {t.value[0]}")
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# tokens = ('ISM_MAWSOL', 'FI3L1', '7ARF_JAR1', 'ISM_MAJROR', 'HAE', 'FI3L2', '7ARF_JAR2', 'MOBTADA2', 'KHABAR', '7AL',
#           'FI3L3', 'MAF3OL_BIH', 'NA2IB_DARF', 'ISM_MAJROR2', 'FAE', 'FI3L4', 'FA3IL', 'FI3L5', 'YAE','ADAT_CHART')


# # Define the regular expressions for each token
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
t_FAE=r'ف'
t_ADAT_CHART=r'لما'
t_FI3L4=r'اشتد'
t_FA3IL=r'ساعد'
t_FI3L5=r'رمان'
t_YAE=r'ي'
# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()

def p_proverb1(p):
    '''proverb : FI3L3 HAE MAF3OL_BIH NA2IB_DARF ISM_MAJROR2 FAE ADAT_CHART FI3L4 FA3IL HAE FI3L5 YAE'''
   
    p[0]=p[1]+p[2]+" "+p[3]+" "+p[4]+p[5]+" "+p[6]+" "+p[7]+p[8]+" "+p[9]+p[10]
     
def p_proverb2(p):
    '''proverb :  MOBTADA2 KHABAR 7AL'''
    p[0]=p[1]+" "+p[2]+" "+p[3]
          
def p_proverb3(p):
    '''proverb : ISM_MAWSOL FI3L1 7ARF_JAR1 ISM_MAJROR FI3L2 7ARF_JAR2 HAE
    '''
    p[0]=p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+p[7]
   
# def p_proverb(p):
#     '''proverb : ISM_MAWSOL FI3L1 7ARF_JAR1 ISM_MAJROR FI3L2 7ARF_JAR2  HAE
#     | MOBTADA2 KHABAR 7AL
#     | FI3L3 HAE MAF3OL_BIH NA2IB_DARF ISM_MAJROR2 FAE ADAT_CHART FI3L4 FA3IL HAE FI3L5 YAE'''
#     if (len(p) == 8):
#       p[0]=p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+p[7]
#     elif (len(p) == 4):
#         p[0]=p[1]+" "+p[2]+" "+p[3]
#     else:
#         p[0]=p[1]+p[2]+" "+p[3]+" "+p[4]+p[5]+" "+p[6]+" "+p[7]+p[8]+" "+p[9]+p[10]
            
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

proverb_input ="مراية الحب عمياء"
proverb = "من شب على شيء شاب عليه"

result = parser.parse(proverb)

print("Parsed proverb:", result)
