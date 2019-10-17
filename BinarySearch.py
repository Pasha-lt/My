# Бинарный поиск это поиск элемента в отсортированном массиве.
# функция будет возращать False если элемент не найдет и номер элемента если он найден.

def binarysearsch(mylist, iskat, start, stop): #Функция принимает лист(где искать), что искать(число), откуда(start) и до куда(stop) искать.
    if start > stop: # возвращаем False если
         return False
    else:
        mid = (start + stop) // 2 #Высчитываем наш mid нам нужно целое число поэтому используем целочисленое деление.
        # вдальнейшем мы будем через mid выражать start и stop
        if iskat == mylist[mid]: # Сравниваем если  iskat равно  mylist[mid] то возвращаем mid
            return mid # mid(также мы можем здесь написать start или stop они совпадают если число есть) У нас при возврате показывает индекс числа
        elif iskat < mylist[mid]: # если цифра которую мы ищем меньше mid
            return binarysearsch(mylist, iskat, start, mid -1) # stop(конечную точку отсчета) будет равен mid - 1 и делаем пересчет
        else:
            return binarysearsch(mylist, iskat, mid + 1, stop) # start(начальную точку отсчета) будет равен mid + 1 и делаем пересчет

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81] # Список в котором будем делать поиск.
iskat = 33 # указываем какую цыфру ищем.
start = 0 # ставим индекс с которого мы начинаем искать первый элемент
stop = len(mylist) # конец списка - длина листа.

x = binarysearsch(mylist, iskat, start, stop) #вызов функции.

if x == False: #проверка если числа нет то пишем что его нет.
    print('Item', iskat, 'Not found!')
else: # иначе пишем его индекс(если нашли).
    print('Item', iskat, 'Found at index', x)