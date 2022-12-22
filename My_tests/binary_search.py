'''#!/usr/bin/env python3

lista = [v for v in range(1, 101)]
print(lista)

 comprobando la busqueda binaria en una lista ordenada 

izq = 0
der = len(lista)


key = 37

while True:
    medio = (izq + der) // 2
    print(medio)
    if lista[medio] == key:
        print(f'ENCONTRADO {key}')
        break
    if lista[medio] > key:
        der = medio 
    
        

    if lista[medio] < key:
        izq = medio 
       '''



'''def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  list.sort()
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = (len(list))//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  
#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False'''




def recursive_binary(my_list, key):

    '''first we sort the list'''
    my_list.sort()
  
    '''then we initialize the left and right for binary search'''
    left = 0
    right = len(my_list) - 1 # we rest 1 for be aliggn with the index of python

    

    '''while lest is less than right the binary search will be doned, if left is greater than right
	    it means that the binary search has finished'''

    while left <= right:

        '''initialize the middle variable'''
        middle = (left + right) // 2
        print(my_list)
        print(middle)

        '''if the len of the list is less than zero it means that the key wasn't found'''
        if len(my_list) == 0:
            print('No se encontro nada')
            return False

        # return true when the middle when ever it will be zero because the list must only have the key    
        elif my_list[middle] == key:
            print('Ya lo encontre')
            return True
        
        # if the middle of the list is less than the key all the left part is deleted
        elif my_list[middle] < key:
            print('Borrando parte izquierda')
            return recursive_binary(my_list[middle+1:], key)

        # if the middle of the list is greater than the key all the right part is deleted
        elif my_list[middle] > key:
            print('Borrando parte derecha')
            return recursive_binary(my_list[:middle-1], key)


foods_list = ['cake', 'bistec', 'salad',
            'spaghetti', 'lasagna', 'meat',
            'yogurt', 'soup', 'coliflower']


recursive_binary(foods_list, 'yogurt')
        

