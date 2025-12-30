def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
 
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile (f_name,l_name,**extra_info):
    user_info = {'first_name': f_name,
                 'last_name': l_name,
                 }
    for k,v in extra_info.items():
        user_info[k] = v
    return user_info
    
print(build_profile('elijah','guma',field= 'engineer',location = 'bida'))

def car_info(manufacturer, model, **add_info):
    info = {'manufacturer': manufacturer,
            'model': model,            
            }
    for k,v in add_info.items():
        info[k] = v
    return info

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
