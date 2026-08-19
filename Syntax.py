"""
print("hello world");
list = [1,2,3,4,5];

for i in list:
    print(i);

    sum = 0
for i in range(1,6,1):
    print(i)
    sum += i
print("sum is: ", sum)

limit = 6
start = 1
sh = 0
while start < limit:
    print(start)
    sh += start
    start += 1

print("sh is: ", sh)

liss = []

for i in range(1,6):
    print(i)
    liss.append(i)
print(liss)

nums = range(1,6) would work too
range(start inclusive, end exclusive, increment value)

for i in range(5): swap range with nums
    print("number " + str( i + 1), end=' ');

init = 0

while init < length:
    print(init, end=' ') used to print a series of things on the same line
    init += 1

"""