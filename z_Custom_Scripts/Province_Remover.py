
while True:
    to_remove : list[str] = input("Input the states TO REMOVE, with spaces between them:\n").split()
    to_remove_from : list[str] = input("Input the states to remove FROM, with spaces between them:\n").split()
    result : list[str] = []
    formatted : str = ""

    for province in to_remove_from:
        if province in to_remove:
            pass
        else:
            result.append(province)
    
    for province in result:
        formatted += f" {province}"

    print("Finished:")
    print(formatted)
    print()