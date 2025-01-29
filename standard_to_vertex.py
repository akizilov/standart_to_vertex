a_term = int(input("A: "))
b_term = int(input("B: "))
c_term = int(input("C: "))
h_number_string = ""
k_number_string = ""

h_number = (b_term/(2*a_term))*-1
k_number = ((h_number**2)*a_term)+(b_term*h_number)+c_term




print("Vertex: ("+str(h_number)+","+str(k_number)+")")

h_number = h_number*-1


if h_number > 0:
    h_number_string = " + "+str(h_number)
else:
    h_number_string = h_number
    
if k_number > 0:
    k_number_string = " + "+str(k_number)
else:
    k_number_string = k_number

print("Vertex form: "+str(a_term)+"(x"+str(h_number_string)+")^2"+str(k_number_string))


