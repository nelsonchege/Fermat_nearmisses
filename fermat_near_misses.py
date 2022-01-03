#creating a function that has two parameters
    # first parameter is for the value of n
    # the second parameter is for the smallest value for x

# for my formula i assume that z will always be larger than either x or y
# i also assume that that x will always be the smallest number out of the three numbers

def fermat(n,range_value):
    # declare three empty variables that will be used inside the for loop
    x = None
    y = None
    z = None

    # this  empty list will contain all the values for the near misses, 
    final_list = []

    for i in range(1,range_value +1):
        # this first for loop will be used to increment the values 
        x=float(i)
        y=float(i)
        z=float(i+1)
       
        for k in range(3,n+1):
            #the formula being used is  x^n + y^n = z^n 
            # below we find the values for x^n ,y^n ,z^n independently
            x_poweredup = x**k
            y_poweredup = y**k
            z_poweredup = z**k

            # add x^n + y^n then divide with z^n
                # in a math equation if you divide the two sides of the equation the answer should be 1
                # but knowing that Fermat's Last Theorem should be equal we are only finding the value closest to 1
            added_value = x_poweredup + y_poweredup
            difference = z_poweredup / added_value
            
            dif = difference - 1 

            # this only converts negative number to positive 
            dif2 = abs(dif)

            # if statement to check if a number is closer to 1 by a difference of 0.1
            if dif2 <= 0.1 :

                # if the difference is less than or equal to 0.1 
                # then the values of x.y.z.n (respectively) are appended to the list created earlier
                final_list.append([int(x),int(y),int(z),k])
        # this is just to increment the values of  y and z      
        y += 1
        z += 1
    print(final_list) 


#ask user for the values of n and range of values for x,y,zs
n = int(input("what is the limit for value for n: "))
range_value = int(input("what is the limit for values for x,y,z: "))

fermat(n,range_value)