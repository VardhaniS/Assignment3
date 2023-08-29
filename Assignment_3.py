#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
We can reuse the code in the functions for multiple times.
It saves the time.
# 2. When does the code in a function run: when it's specified or when it's called?
The code of the function run when the function is called.
In the below example u can see the code is the function not executed first the main programme had run then when the function is called the code in function executed.
# In[6]:


def add():
    add=4+5
    print("Function called")
    return add

print("calling the function")
x=add()
print(x)


# 3. What statement creates a function?
def keyword created the function.
# 4. What is the difference between a function and a function call?
 A function consists of set of code .
 Function call is used to execute the set of code inside the function.
 Without function call the code inside the function can't be executed.
# 5. How many global scopes are there in a Python program? How many local scopes?
In python programming we will be having only one global scope.
We can have many local scopes as per the no. of function used in the program
# 6. What happens to variables in a local scope when the function call returns?
When the function call returns it returns the value .
# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
The return is a statement that returns the value next to it. We can store the return value in any variable outside the function. Yes it possible to have.
# 8. If a function does not have a return statement, what is the return value of a call to that function?
it will be undefined 
# 9. How do you make a function variable refer to the global variable?
By accessing the globale variable. The global variable can be accessed from everywhere of the program even from the inside the function
# 10. What is the data type of None?
None is a keyword. Nontype is the data type
# 11. What does the sentence import areallyourpetsnamederic do?
Imports the module named areallyyourpetsnamederic
# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
spam.bacon()
# 13. What can you do to save a programme from crashing if it encounters an error?
run the program
# 14. What is the purpose of the try clause? What is the purpose of the except clause?
We use try and except for error handling. We write a block of code and if want to excecute it even if error occured we use try and except . try caluse is used to run the code and if error occured except will print the code given in the except clause.
# In[ ]:




