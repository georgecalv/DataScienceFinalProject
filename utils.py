def convert_temp(temp):
    '''
    this method takes in a temp that is in celsius 
    and converts it to farenheit
    '''
    convert = (temp * (9/5)) + 32 
    convert = round(convert, 2)
    return convert
