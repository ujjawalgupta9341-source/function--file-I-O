# 1.WAF to print the length of  list.(list in the parameter)
names=['raj','suraj','biocorn','corncord']
a=['ram', 'shyam','mohan']
def list(names):
    print(len(names))
   
list(names)
list(a) 

#2. WAF to print the elements of list in a single line .(list in the parameter)

name=['ujjawal','raj','suraj','priya']

def list(name):
    for i in name:
        print(i, end=",")

list(name)

#3.WAF to find the factorial of n.(n is the parameter)

def fact(n):
    mult=1
    for i in range(1,n+1):
     mult= mult * i
    print(mult)
    return mult
fact(5)
fact(7)


#4. WAF to convert $ to INR

def currency(a):
    usd=95.94
    inr=usd*a
    print("INR",inr)
currency(5)

        
    
# #5create a file 'demo.txt' using python . add the data in it 
with open("demo.txt","w") as f:
     f.write( 'hii everyone''\nwe are learning File I/O')
     f.write('\nusing Java.''\nI like programming in Java')
            
#6 WAF that replacee all occurences of 'Java' with 'Python' in above file.
def file():
 with open("demo.txt","r") as f:
    data=f.read()
    new_data=data.replace('Java','Python')
    print( new_data)
 with open("demo.txt","w") as f:
    f.write(new_data)
file()
#7 search if the word 'learning ' exists in the file or not..
with open('demo.txt','r') as f:
   data=f.read()
   new=data.find('learning')
   if new!=-1:
      print("found")
   else:
      print("not found")

