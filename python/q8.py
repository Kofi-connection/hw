ones=dict()
ones['one']=1
ones['two']=2
ones['three']=3
ones['four']=4
ones['five']=5
ones['six']=6
ones['seven']=7
ones['eight']=8
ones['nine']=9
ones['ten']=10

tens=dict()
tens['eleven']=11
tens['twelve']=12
tens['thirteen']=13
tens['fourteen']=14
tens['fifteen']=15
tens['sixteen']=16
tens['seventeen']=17
tens['eighteen']=18
tens['ninteen']=19
tens['twenty']=20
tens['thirty']=30
tens['forty']=40
tens['fifty']=50
tens['sixty']=60
tens['seventy']=70
tens['eighty']=80
tens['ninety']=90


ip= raw_input('Enter a number less than 100:')
print (ip)
numbers=ip.split()
if numbers[0] in ones and numbers[1] in ones:
   print('The product is')
   print(ones[numbers[0]] * ones[numbers[1]])
elif numbers[0] in ones and numbers[1] in tens:
   print('The product is')
   print(ones[numbers[0]] * tens[numbers[1]])
elif numbers[0] in tens and numbers[1] in ones:
   print ('The product is')
   print (tens[numbers[0]] * ones[numbers[1]])
elif numbers[0] in tens and numbers[1] in tens:
   print ('The product is')
   print (tens[numbers[0]] * tens[numbers[1]])
else:
    print('Number not in dictionary')


