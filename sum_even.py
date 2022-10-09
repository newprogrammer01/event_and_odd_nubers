#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

var_int=6780
x1=var_int//1000
x2=var_int%100//10
x3=var_int%10
sum_even=x1+x2+x3
print(sum_even)
