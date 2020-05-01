# importing pandas package 
import pandas as geek 
	
# making data frame from csv file 
data = geek.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
	
# Integer slicing 
print("Slicing only rows(till index 4):") 
x1 = data.ix[:4, ] 
print(x1, "\n") 

print("Slicing rows and columns(rows=4, col 1-4, excluding 4):") 
x2 = data.ix[:4, 1:4] 
print(x2) 
