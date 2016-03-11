import fake_database

CACHE = {}

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
	
    if "last5" not in CACHE:
        CACHE["last5"] = []

    if len(CACHE.get("last5")) < 5:
        last5_lst = CACHE.get("last5")
        last5_lst += ['{} * {} = {}'.format(a, b, result)]
        CACHE["last5"] = last5_lst
    else:
        last5_lst = CACHE.get("last5")
        last5_lst = last5_lst[1:]
        last5_lst += ['{} * {} = {}'.format(a, b, result)]
        CACHE["last5"] = last5_lst
            

def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: list last multiplied result
    This is list of the last 5 multiplied questions/answers
    """
    return CACHE.get("last5", [])


def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    store answer in CACHE. also have a key of "last5" and val is a list. 
    """
    cache_key = (a,b)

    if cache_key in CACHE:
        answer = CACHE.get(cache_key)
    
    else:
        answer = fake_database.russian(a,b)
        CACHE[cache_key] = answer

    updateLastMultiplied(a,b, answer)

    return answer

if __name__ == '__main__':
    print multiplyHandler(4, 2)
    print multiplyHandler(3, 2)
    print multiplyHandler(5, 5)
    print multiplyHandler(10, 5)
    print multiplyHandler(3, 4)
    print multiplyHandler(4, 2)
    print lastMultipliedHandler()


