import html
str = '\\u0'
output = '{'
for i in range(2304, 2431):
    rig = hex(i).lstrip('0x')
    output =output + ' : ' '\'' + str + rig + '\'' + ','

output =  output + '}'
print(output)

print('\u0918\u094d\u092f')
print('\u200d')
print('\u0971')
print('\u005c')
print('\u0930')
print('\u0924\u0930\u094d')
print('\u096f''\u005c''\u097d')
print(html.unescape('&#2346;&#2381;&#2352;&nbsp;&#2358;&#2381;&#2352;&nbsp;&#2332;&#2381;&#2334;&nbsp;&#2340;&#2381;&#2352;&nbsp;&#2352;&#2369;&nbsp;&#2352;&#2370;&nbsp;&#2329;&nbsp;.'))