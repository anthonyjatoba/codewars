def get_drink_by_profession(param):
    dict = {"jabroni": "Patron Tequila",
            "school counselor": "Anything with Alcohol",
            "programmer": "Hipster Craft Beer",
            "bike gang member": "Moonshine" ,
            "politician": "Your tax dollars" ,
            "rapper": "Cristal"}
    
    return dict.setdefault(param.lower(), 'Beer')