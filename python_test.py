#Question1
x = [100,110,120,130,140]
newlist = []

for a in x:
    newlist.append(a * 5)

print(newlist)


#question2
def divisible_by_three(n):
    for num in range(n):
         if num % 3 == 0:
              print(f"{num} is divisible by 3")
         else:
             print(f"{num} is not divisible by 3")  

divisible_by_three(100)  

#Question3
x = [[1,2],[3,4],[5,6]]
def flatlist(xList):
    if len(xList) == 0:
        return xList
    if isinstance(xList[0], list):
        return flatlist(xList[0]) + flatlist(xList[1:])
    return xList[:1] + flatlist(xList[1:])


print(flatlist([[1,2],[3,4],[5,6]]))

#Question4
def smallest():
    list1 = [3,6,8,2,4,1,5,7]
    list1.sort()
    print( list1[:1])

smallest()

#question5
x= ['a','b','a','e','d','b','c','e','f','g','h']
y = {'a','b','a','e','d','b','c','e','f','g','h'}
print(y)


#Question6
def divisible_by_seven():
    for r in range(100,200):
        if r%7==0:
            print(f"{r} is divisible by seven")
        else:
            print(f"{r} is not divisible by seven")

divisible_by_seven()                



#question7
 

def greetings():
    students=[{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}]
    for x in students:
        age=x["age"]
        name=x["name"]
        year=2021-age
    print(f"Hello {name} you were born in the year {year}.")
greetings()


class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    

    def area(self):
        A=self.width*self.length
        return f"{A}"
    
    def perimeter(self):
        P=((2*self.length)+(2*self.width))
        return f"{P}"

        
 


