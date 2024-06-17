D = {1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
print("THE DICTIONARY IS :",D)
D[8]=8.8
print("After adding : ",D)
del D[2]
print("After removing key 2 :",D)
print("Check whether 6 key is present :",6 in D)
print("The number of element in D :",len(D))
print("Sum of all elements is :",sum(D))
D[3] = 7.1
print("After updating :",D)
D.clear()