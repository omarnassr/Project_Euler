'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
#Forming an iterable data form to hold the date.
List1 = list(range(1000))
#Counter starting from 0 as it natural numbers only.
sum = 0
#For loop iterated over the list
for i in List1:   
            #conditions required with OR statement.         
            if i % 3 == 0 or i %5 == 0:
                # If I matches then add it to sum every time it match. 
                sum += i 
#git the results                    
print(sum)
        

