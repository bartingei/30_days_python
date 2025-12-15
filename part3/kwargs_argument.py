# using both **kwargs (stores data as a dictionary)   and *args (stores data as a tuple)

def shipping_label(*args,**kwargs):             #should follow order of args then kwargs
    
    #iterating thru the args first
    print("-" * 60)
    print("\t these are the *args values")
    print("-" * 60)

    for arg in args:
        print(f"{arg}", end=" ")
    print()


    print("-" * 60)
    print("\t these are the **kwargs values")
    print("-" * 60)

    """ 
        for key, value in kwargs.items():
        print(f"{key} => {value}")
    """
    if 'apartment' in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apartment')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('Town')},{kwargs.get('zip')}")
    



shipping_label(
    "Dr.", "Johnpaul", "Kibet", "Bartingei",
    #kwargs now
    street = "Njambi road",
    apartment = "Jolemu Boma f23",
    city = "Ongata",
    Town = "Rongai",
    zip = 543132
)