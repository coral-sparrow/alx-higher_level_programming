counter = 0
def magic_string():
    global counter 
    counter += 1
    return ', '.join(['BestSchool'] * (counter - 1))
