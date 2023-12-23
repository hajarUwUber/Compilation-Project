from ply import lex

# Define the token names
tokens = ('MOBTADAE', 'MODAF', 'KHABAR' , 'ISM' , 'FI3L' ,'MAF3OULBIH' ,'HAL' , 'BADAL' , 'HARF' , 'DAMIR' )

# Define the regular expressions for each token
t_MOBTADAE = r'(?:حبل|الدهر)'
t_MODAF = r'الكذب'
t_KHABAR = r'(?:قصير|يومان)'
t_ISM = r'(?:من|يوم)'
t_MAF3OULBIH = r'الناس'
t_FI3L = r'(?:مات|راقب)'
t_HAL = r'همًا'
t_HARF = r'(?:ل|علي|و)'
t_DAMIR = r'ك'


# من: اسم شرط جازم مبني على السكون في محل رفع مبتدأ.
# راقب: فعل ماض مبني على الفتح الظاهر على آخره، وهو في محل جزم، والفاعل ضمير مستتر جوازاً تقديره هو.
# الناس: مفعول به منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
# مات: فعل ماض مبني على الفتح الظاهر على آخره، والفاعل ضمير مستتر تقديره هو.
# هماً: حال منصوب وعلامة نصبها الفتحة الظاهرة على آخره.
# جملة (راقب): جملة فعلية استئنافية لا محل لها من الإعراب.
# جملة (مات): جملة جواب الشرط الجازم غير المقترن بالفاء لا محل لها من الإعراب.

# الدهر: مبتدأ مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
# يومان: خبر مرفوع وعلامة رفعه الألف لأنه مثنى، والنون بدل التنوين في الاسم المفرد.
# يوم: بدل تفصيل مرفوع وعلامة رفعه الضمة الظاهرة على آخره
# اللام: حرف جر مبني على الفتح يفيد الملكية.
# الكاف: ضمير متصل مبني في محل جر بحرف الجر (اسم مجرور).
# الواو: حرف عطف مبني على الفتح يفيد الجمع والمشاركة.
# يوم: اسم معطوف مرفوع وعلامة رفعه الضمة الظاهرة على آخره.
# على: حرف جر مبني على السكون يفيد الاستعلاء
# الكاف: ضمير متصل مبني في محل جر بحرف الجر (اسم مجرور)



# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
    
lexer = lex.lex()

# Test the lexer with the proverb
proverb1 = "حبل الكذب قصير"
proverb2 = "من راقب الناس مات همًا"
proverb3 ="الدهر يومان يوم لك ويوم عليك"


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
