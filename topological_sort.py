# my implementation of topological sort (τοπολογικη διαταξη)
# using a linked list
# using python

#elemements
from linked_list import LinkedList

v = [1,2,3,4,5,6,7,8,9]
#partial order
#[index][1] -> element
#[index][0] -> prereq for element
u = [(1 ,2) ,(1 ,6) ,(2 ,6) ,(3 ,1) ,(3 ,7) ,(4 ,1) ,(4 ,7) ,(5 ,2) ,(5 ,8) ,(6 ,9) ,(3 ,8) ,(8 ,9)]

#initialize sort with the prereq of u[1]
sort = LinkedList(u[0][0])
#insert the u[1] after the prereq
sort.insert(u[0][1])

#sort the remaining of u
for p in u[1::]:
    prereq = p[0]
    el = p[1]
    prereq_index = sort.get_index(prereq)
    el_index = sort.get_index(el)
    
    if(el_index == -1 and prereq_index == -1):
        sort.insert(prereq)
        sort.insert(el)
    elif(el_index == -1 and prereq_index != -1):
        sort.insert(el, prereq_index + 1)
    elif(el_index != -1 and prereq_index == -1):
        sort.insert(prereq, el_index)
    elif(prereq_index > el_index):
        sort.swap_values(prereq_index, el_index)

sort.print_els()