# Python Gist

## Future

Future sempre são chamadas de baixo nível aguardando chamada de alto nível.
Um Future representa um resultado final de uma operação assíncrona.
O Future é um objeto de mais baixo nível

A Task é de alto nível
A Task é um objeto que é agendado para ser executado no event loop

O Event Loop, essencialmente, tem a finalidade de aguardar a ocorrência de 
eventos antes de corresponder cada evento a uma função que correspondemos 
explicitamente ao tipo de evento.

O Event Loop registrar, executar e cancelar chamadas

O Event Loop Iniciar subprocessos e transportes associados para comunicação com um programa externo

O Event Loop Delegar chamadas de função dispendiosas a um conjunto de threads

Tanto o Future quanto a Task, são uma Task

O Event Loop é o gerenciador de Tasks

***

## Cheatsheet

### Interact with the user (input and output)

**Print a message**
```print('Hello, world!')```

**Print multiple values (of different types)**
```
ndays = 365
print('There are', ndays, 'in a year')
```

**Asking the user for a string**
```name = input('What is your name? ')```

**Asking the user for a whole number (an integer)**
```num = int(input('Enter a number: '))```

### Decide between options

**Decide to run a block (or not)**
```
x = 3
if x == 3:
    print('x is 3')
```
**Decide between two blocks**
```
mark = 80
   if mark >= 50:
     print('pass')
   else:
print('fail')
```
**Decide between many blocks**
```
mark = 80
   if mark >= 65:
     print('credit')
   elif mark >= 50:
     print('pass')
   else:
print('fail')
```

- elif can be used without else
- elif can be used many times

**Are two values equal?**
```x == 3```
NOTE: Two equals signs, not one

**Are two values not equal?**
```x != 3```

**Less than another?**
```x < 3```

**Greater than another?**
```x > 3```

**Less than or equal to?**
```x <= 3```

**Greater than or equal to?**
```x >= 3```

**The answer is a Boolean:**
```True``` **or** ```False```

### String manipulation

**Compare two strings**
```
msg = 'hello'
   if msg == 'hello':
print('howdy')
```

**Less than another string?**
```
if msg < 'n':
    print('a-m')
else:
    print('n-z')
```
NOTE: Strings are compared character at a time (lexicographic order)

**Is a character in a string?**
```'e' in msg```

**Is a string in another string?**
```'ell' in msg```

**Convert to uppercase**
```msg.upper()```
NOTE: Also **lower** and **title**

**Count a character in a string**
```msg.count('l')```

**Replace a character or string**
```msg.replace('l','X')```

**Delete a character or string**
```msg.replace('l','')```

**Is the string all lowercase?**
```msg.islower()```
NOTE: Also **isupper** and **istitle**

### Text (strings)

**Single quoted**
```'perfect'```

**Double quoted**
```"credit"```

**Multi-line**
```
'''Hello,
   World!'''
```

**Add (concatenate) strings**
```'Hello' + 'World'```

**Multiply string by integer**
```'Echo...'*4```

**Length of a string**
```len('Hello')```

**Convert string to integer**
```int('365')```

### Variables

**Creating a variable**
```celsius = 25```

**Using a variable**
```celsius*9/5 + 32```

### Whole numbers (integers)

**Addition and subtractio**
```365 + 1 - 2```

**Multiplication and division**
```25*9/5 + 32```

**Powers (2 to the power of 8)**
```2**8```

**Convert integer to string**
```str(365)```

### Repeat a block (a fixed number of times)

**Repeat a block 10 times**
```
for i in range(10):
     print(i)
```

**Sum the numbers 0 to 9**
```
total = 0
   for i in range(10):
     total = total + i
   print(total)
```

**Repeat a block over a string**
```
for c in 'Hello':
    print(c)
```

**Keep printing on one line**
```
for c in 'Hello':
     print(c, end=' ')
print('!')
```

**Repeat a block over list (or string) indices**
```
msg = 'I grok Python!'
   for i in range(len(msg)):
print(i, msg[i])
```

**Count from 0 to 9**
```range(10)```
NOTE: range starts from 0 and goes up to, but not including, 10

**Count from 1 to 10**
```range(1, 11)```

**Count from 10 down to 1**
```range(10, 0, -1)```

**Count 2 at a time to 10**
```range(0, 11, 2)```

**Count down 2 at a time**
```range(10, 0, -2)```

### Putting it together: Celsius to Fahrenheit converter

**Ask the user for a temperature in degrees Celsius**
```celsius = int(input('Temp. in Celsius: '))```

**Calculate the conversion**
```fahrenheit = celsius*9/5 + 32```

**Output the result**
```print(farenheit, 'Fahrenheit')```

***
