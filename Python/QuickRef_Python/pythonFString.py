website = "quick Test"
print(f'{website} for abhishek')

num = 10 
print(f'{num} + 10 = {num + 10}')

print(f"""He said {"I'm John"}""") 

print(f'5 {"{stars}"}')

print(f'{{5}} {"stars"}')

name = 'Eric'
age = 31
f"""hello
    my name is {name}
    i"am {age}"""
  
  
print(f'{"text":0}')       # [width]
print(f'{"text":*>10}')    # fill left
print(f'{"text":*<10}')    # fill right
print(f'{"text":*^10}')    # fill center
print(f'{12345:0>10}')     # fill with number 

print(f'{10:b}') # binary type
print(f'{10:o}') # octal type
print(f'{200:x}') # hexadecimal type
print(f'{200:X}') # hexadecimal type
print(f'{345600000000:e}') 
print(f'{65:c}')
print(f'{10:#b}')
print(f'{10:#o}')
print(f'{10:#x}')

print(f'{-12345:0=10}')  # negative numbers add zero at front
print(f'{12345:010}')
print(f'{-12345:010}') 

import math 
print(math.pi)
print(f'{math.pi:.2f}')

print(f'{1000000:,.2f}') # grouping option at float level

print(f'{1000000:_.2f}')
print(f'{0.25:0%}')      # percentage

print(f'{0.25:.0%}') 
   
print(f'{12345:+}')
print(f'{-12345:+}')
print(f'{-12345:+10}')
print(f'{-12345:+010}')


