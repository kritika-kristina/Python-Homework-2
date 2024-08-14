# Question 1
x = int(input("Enter a number: "))

if x % 2 == 0:
    print(x, 'is even')
else:
    print(x,'is odd')

# Question 2 

y = int(input("Enter a number: "))

if y % 7 == 0:
    print(y ,'is divisible by 7')
else:
    print(y,'is not divisble by 7')
    
# Question 3

num = int(input("Enter a number: "))

if num % 5 == 0:
    print('hello')
else:
    print('bye')
    
# Question 4

marks = int(input("Enter a number: "))

if marks > 80:
    print('A+ grade')
if 80 > marks > 70:
    print('A grade')
if 70 > marks > 60:
    print('B Grade')
if 60 > marks > 50:
    print('C grade')
if marks < 50: 
    print('fail')
    
# Question 5 

a = 1 

while a <= 10:
    print(a)
    a += 1 

# Question 6 

b = 4
limit = 10

print('Multiplication table for' , b)
for i in range(1, limit + 1):
    result = b * i 
    print(b, "x", i, "=", result)

# Question 7 
c = -10 

while c <= -1:
    print(c)
    c += 1

# Question 8 

d = list(range(0,11,2))
print(d)

#Question 9 

st = 'Print every word in this sentence that has an even number of letters'
words = st.split()

for word in words:
    if len(word) % 2 == 0:
        print(word, "even!") 
    