# keyword arguments = an argument preceded by an identifier... it helps with readability, the order of arguments do not matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{ first} {last}")

hello("hello", "Mr.", "JP", "Kibet")