x = [7,6,5,4,3,2,1]

N = len(x)
z = 0
b = 0

while (z < N-1):
    b = 0   
    while (b < N-1):
        mi = b
        tek1 = x [mi]
        sled2 = x [mi+1]

        if sled2 < tek1 :
            x [mi] = sled2
            x [mi+1] = tek1
        b = b + 1
     
    z = z + 1

y = int(input("Введите число, которое нужн опроверить на наличие в массиве "))
print(x)
print(y, "нужно проверить на совпадение с числом массива")
mLen = len(x)
print("Длина массива равна", mLen)
left = x[0]         # значение числа с левой части массива
right = x[mLen - 1] # значение числа с правой части массива
indLeft = 0         # значение индекса левой позиции массива
indRight = mLen - 1 # значение индекса правой позиции массива
middle = 0          # значение центрального числа массива
indMiddle = 0       # индекс середины отрезка

# функция поиска индекса середины отрезка в массиве
def Seredina_Massiva (indLeft, indRight):         
    indMiddle = indRight + indLeft
    print("Длинна массива до деления ", indMiddle)
    indMiddle = indMiddle // 2
    print("Длина массива после деления ", indMiddle)
    return indMiddle

# функция определения где число относительно середины отрезка в массиве(справа, слева или совпадает с серединой)
def Gde_chislo(indMiddle):
    if y == x[indMiddle]:
        k = 0            # Y совпадает с серединой отрезка
    elif y < x[indMiddle]: 
        k = 1            # Y левее середины отрезка
    elif y > x[indMiddle]:
        k = 2            # Y правее середины отрезка
    return k
flag = 1
# цикл деления отрезка пополам
if (y < x[indLeft]):
    print("Число находится вне массива слева")
    flag = 0
elif (y > x[indRight]):
    print("Число находится вне массива справа")
    flag  = 0
else:
   print("Искомое число находится внутри массива, но не факт, что возможно совпадение")
if left == y:
    print("Искомое число находится в начале массива и его индекс", indLeft)
    flag = 0
if right == y:
    print("Искомое число находится в конце массива и его индекс",indRight)
    flag = 0
while flag == 1:
    indMiddle = Seredina_Massiva(indLeft, indRight)
    print("Индекс середины отрезка ", indMiddle)
    middle = x[indMiddle]
    print("Значение в середине отрезка равно", middle)

    a = Gde_chislo(indMiddle)
    print("Признак где число", a)

    if a == 0 :                                                 # Y совпадает с серединой отрезка
       print("Число есть в массиве и его индекс", indMiddle)
       print("Само число равно", x[indMiddle])
       flag = 0                                                 # останавливаем выполнение программы
    elif a == 1 :                                               # Y левее середины отрезка
        indRight = indMiddle
    elif a == 2:                                                # Y правее середины отрезка
        indLeft = indMiddle
    if indRight - indLeft == 1:                                 # делаем проверку что осталось только 2 числа => между ними никаких чисел нет
       print("В отрезке осталось 2 числа и этот отрезок нельзя делить пополам. Искомое число в массиве не найдено")
       flag = 0  
