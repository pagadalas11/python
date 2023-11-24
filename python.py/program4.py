#zip function
names= [
    "rishi",
    "Devi",
    "Santosh"]
age= [26, 25, 23]
gender= ["male", "female", "male"]

# create a function  
all_details= list(zip(names, age, gender))
print(all_details)

for n,a,g in all_details:
    print(n)
    print(a)
    print(g)

    # new program 

    a= [1,2,3]
    b=a
    print(b==a) 