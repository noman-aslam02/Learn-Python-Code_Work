#Comments in Python

#Single-Line Comment
#may ek single line comment hu
print("My name is Muhammad Noman Aslam")



#Multiple-Line Comment
"""
may ek multiple line comment hu
yeh lu dusri line
yeh lu teesri line
"""
'''
may ek multiple line comment hu
yeh lu dusri line
yeh lu teesri line
'''
print("Aaj ka moosam bohut acha hai")

#Tip hum code ko bhi comment kr sakhte hai, yeh code execute nhi hogha
#print("Mujehy comment krdo mera koi kaam nhi")

#Escape Sequences

#Backslash Character
print("Backslash \\") #output : Backslash \

#Single Quote
print("Single Quote \'") #output : Single Quote '

#Double Quote
print("Double Quote \"") #output : Double Quote "

#NewLine Character
print("My name is noman and \nscooby scooby doo")#output : #My name is noman and
                                                           #scooby scooby doo
#Important note!
# ab hum yaha pr kudh say new line k liay enter mar kr newline nhi de sakhte
"""
print("My name is noman and
      scooby scooby doo")
"""
"""
yeh syntax error issliay aya q k python code may python kudh say kssi ko allow nhi krta k enter kr
k newline lee aey bulke hamay escape sequence \n ka astmaal kr k newline deni hoti hai
"""
#Tab Character
print("Hello\tWorld") #output: Hello	World
#yeh 3 times space deta hai yaani tab character insert krta hai

#Backspace Character
print("Hello \bWorld") #output :HelloWorld

#Carriage Return
print("Hello \rWorld") #output : World
#it will remove all word joo \r say phele likhe huwe hai


#Print Statement
"""
maan lo hamaray paas ek variable may string value hai aur ek integer value hai to jab hum ussay
print krwaenghay to kuch iss format may krwaenghay jssko hum print statement bolte hai 
"""
x = 21
y = "Aslam"
print("Noman",y,"Age is",x)
#yaha integer value python kudhi convert kr k string may likh deta hai