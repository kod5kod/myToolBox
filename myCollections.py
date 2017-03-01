
# Everyday functions

def seconds_to_hms(seconds):
    """ 2017-02-07
    input: seconds (int)
    output: "h:m:s" string
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return  "%d:%02d:%02d" % (h, m, s)

def hexa_sha1(string):
    """ 2017-02-07
    input: a string to be hashed (str)
    output: a hexadecimal hash1 type hash of the input string (str)
    """ 
    import hashlib
    m = hashlib.sha1()
    m.update(('hhid_'+string).lower())
    return     m.hexdigest()

def check_idfa(idfa_string):
    """ 2017-02-07
    input: A string to be checked for IDFA format (str)
    Output: True if input matches IDFA format, False otherwise (str)
    """
    import re
    idfa_pattern = '[0-9a-fA-F]{8}[-][0-9a-fA-F]{4}[-][0-9a-fA-F]{4}[-][0-9a-fA-F]{4}[-][[0-9a-fA-F]{12}'
    return True if ((re.match(idfa_pattern, idfa_string) and (len(idfa_string)==36)) and not (idfa_string=='00000000-0000-0000-0000-000000000000') ) else False   
   
def print_factors(x):
    """ 2017-02-07
    # This function takes a number and prints its factors
    """
    factors = []
    for i in range(1, x ):
        if x % i == 0:
            factors.append(i)
    return (factors)

def list_slicer(list_to_slice):
    """ 2017-02-19
    """
    number=len(list_to_slice)
    a = number%1000 
    x = number- a
    number=a
    b = number%100 
    y = number- b
    number=b
    c = number%10 
    z = number- c 
    #print 'x,y,z,c:',x,y,z,c
    if x:
        return {'1000':list_to_slice[:x],'100':list_to_slice[x:x+y],'10':list_to_slice[x+y:x+y+z],'1':list_to_slice[x+y+z:]}
    if y:
        return {'100':list_to_slice[:y],'10':list_to_slice[y:y+z],'1':list_to_slice[y+z:]}
    if z:
        return {'10':list_to_slice[:z],'1':list_to_slice[z:]}
    if c:
        return {'1':list_to_slice}

    
def number_rounder(length_of_list):
    """ 2017-02-19
    Rounds the number to nearest 1k,500, or 100 devisible number
    example: if number is 24,945, the number will be rounded to 24,000
             if number is 846, the number will be rounded to 500
             if number is 243, the number will be rounded to 200
    """
    if length_of_list >=1000:
        rounded = int(round(length_of_list / 1000) * 1000)
        or_number = 1000-1
    elif length_of_list >=500 and length_of_list < 1000:
        rounded = int(round(x / 500) * 500)
        or_number = 500-1
    elif length_of_list>=100 and length_of_list<500:
        rounded =  int(round(length_of_list / 100) * 100)
        or_number = 100-1
    elif length_of_list>=10 and length_of_list<100:
        rounded =  int(round(length_of_list / 10) * 10)
        or_number = 10-1
    else:
        rounded = length_of_list-1
        or_number = 0
    return rounded, or_number

