s = 'awdawd'
is_s_Int = True

try:
   # converting to integer
   int(s)
except ValueError:
   is_s_Int = False
   
if is_s_Int:
   print('Input value is an integer')
else:
   print('Not an integer')