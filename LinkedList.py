# #program to remove dups in the list with O(n2) complexity
# def RemoveDups(h):
# 	if h==None:
# 		return
# 	while(h!=None):
# 		v=h.value
# 		n=h.next
# 		prev=h
# 		while(n!=None):
# 			if n.value==v:
# 				prev.next=n.next
# 				break
# 			prev=n
# 			n=n.next
# 		h=h.next
# RemoveDups(head)
# printing(head)




class Node:
	def __init__(self,key):
		self.next=None
		self.value=key
head=Node(10)

#program to insert
def insert(h,value):
	if h==None:
		h.value=value
		return
	while(h.next!=None):
		h=h.next
	h.next=Node(value)
	
insert(head,20)
insert(head,30)
insert(head,30)
insert(head,50)
insert(head,50)
insert(head,20)
insert(head,70)

#program to print the list
def printing(h):
	if h==None:
		return
	while(h!=None):
		print(h.value)
		h=h.next



# #program to remove dups in the list with O(n) complexity
def RemoveDups(h):
	d={}
	if h==None:
		return 
	prev=None
	while(h!=None):
		if(h.value in d):
			prev.next=h.next
		else:
			d[h.value]=1
			prev=h

		h=h.next
RemoveDups(head)
printing(head)











