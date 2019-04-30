def limit(num): #defining function that makes the limits/parameters
    if num < 0: #if the number taken is less than 0....
        return 0 #return 0
    if num > 255: #if the number taken in is greater than 255...
        return 255 #return 255
    return num #return the number


def rgb(r, g, b): #defining function that takes in different values for red, green, and blue.
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b)
    #Python already has an algorithm fhat formats  three numbers for R G B in to 2 digit hexadeciamal strings.
    #If the limits/conditions are met, then plug in values for RGB, and get answer.
