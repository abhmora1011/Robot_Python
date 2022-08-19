# kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title='Mr.',first='Abe',last='Ora')

# Hello Abe Ora
# Mr. Abe Ora