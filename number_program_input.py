def word_to_number(word):
    if word == 'one':
        return(1)
    elif word == 'two':
        return(2)
    elif word == 'three':
        return(3)
    elif word == 'four':
        return(4)
    elif word == 'five':
        return(5)
    elif word == 'six':
        return(6)
    elif word == 'seven':
        return(7)
    elif word == 'eight':
        return(8)
    elif word == 'nine':
        return(9)
    elif word == 'ten':
        return(10)
    elif word == 'eleven':
        return(11)
    elif word == 'twelve':
        return(12)
    elif word == 'thirteen':
        return(13)
    elif word == 'fourteen':
        return(14)
    elif word == 'fifteen':
        return(15)
    elif word == 'sixteen':
        return(16)
    elif word == 'seventeen':
        return(17)
    elif word == 'eighteen':
        return(18)
    elif word == 'nineteen':
        return(19)
    elif word == 'twenty':
        return(20)
    elif word == 'thirty':
        return(30)
    elif word == 'forty':
        return(40)
    elif word == 'fifty':
        return(50)
    elif word == 'sixty':
        return(60)
    elif word == 'seventy':
        return(70)
    elif word == 'eighty':
        return(80)
    elif word == 'ninety':
        return(90)
    elif word == 'hundred':
        return(100)
    elif word == 'thousand':
        return(1000)
    elif word == 'million':
        return(1000000)
    elif word == 'billion':
        return(1000000000)

def chinese_character_to_arabic_number(character):
    if character == '一':
        ## '\u4e00'
        return(1)
    elif character == '二':
        ## '\u4e8c'
        return(2)
    elif character == '三':
        ## '\u4e09'
        return(3)
    elif character == '四':
        ## '\u56db'
        return(4)
    elif character == '五':
        ## '\u4e94'
        return(5)
    elif character == '六':
        ## '\u516d'
        return(6)
    elif character == '七':
        ## '\u4e03'
        return(7)
    elif character == '八':
        ## '\u516b'
        return(8)
    elif character == '九':
        ## '\u4e5d'
        return(9)
    elif character == '十':
        ## '\u5341'
        return(10)
    elif character == '百':
        ## '\u767e'
        return(100)
    elif character == '千':
        ## '\u5343'
        return(1000)
    elif character == '万':
        ## '\u4e07'
        return(10000)
    elif character == '萬':
        ## '\u842c'
        return(10000)
    elif character == '億':
        ## '\u5104'
        return(100000000)
    elif character == '亿':
        ## '\u4ebf'
        return(100000000)
    elif character == '兆':
        ## '\u5146'
        return(1000000000000)

sample_arabic_number_strings = ['Five hundred million two hundred three thousand seventeen', 'One billion seventy three', 'One hundred ninety two thousand seven hundred thirty one']

sample_chinese_number_strings = ['九万二千三百二十一','九千二百万二千三百二十一','九亿八千万四百八十一']
## 92,321; 92,002,321; 980,000,481
