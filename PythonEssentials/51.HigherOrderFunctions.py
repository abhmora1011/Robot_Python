#python #higher-order #functions

#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()



def hello(func, name):
   text = func(name)
   print(text)


hello(loud, "Abe") # ABE
hello(quiet, "Gale") # gale

# ------------ 2. returns a function -------------
def divisor(x):
   def dividend(y):
       return y / x
   return dividend


divide = divisor(2)
print(divide(10)) # 5.0
