list1 = []

while True:
    num = int(input('Enter a number(or -1 to quit): '))
    if num != -1:
        list1.append(num)
    else:
        break

print('There are %d numbers.' % len(list1))
print('The biggest number is %d.' % max(list1))
print('The smallest number is %d.' % min(list1))
print('The sum is %d.' % sum(list1))
print('From biggest to smallest in sequence: ' + str(format(sorted(list1, reverse=True))) + '.')