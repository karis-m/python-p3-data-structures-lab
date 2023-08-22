spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
spicy_food ={
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
def get_names(spicy_foods):
    
    res = [val['name'] for val in spicy_foods]
    print(str(res))
    return res

def get_spiciest_foods(spicy_foods):
    res = [val for val in spicy_foods if val['heat_level']>5]
    print(str(res))
    return res


def print_spicy_foods(spicy_foods):
    pep = "🌶"
    # update = {'heat_level':pep * val['heat_level'] for val in spicy_foods}
    new_dicts = [{**d,**{'heat_level':pep * d['heat_level'] for d in spicy_foods}} for d in spicy_foods]
    print(str(new_dicts))
    return new_dicts

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    res = [val for val in spicy_foods if cuisine == val['cuisine']]
    print(str(res))
    return res

def print_spiciest_foods(spicy_foods):
    res = [val for val in spicy_foods if val['heat_level']>5]
    print(str(res))
    return res

def get_average_heat_level(spicy_foods):
    res = [val['heat_level'] for val in spicy_foods]
    average = sum(res) / len(res)
    print(average)
    return average
def create_spicy_food(spicy_foods, spicy_food):
    res = [spicy_foods.append(spicy_food)]
    print(res)
    return res
get_names(spicy_foods)
get_spiciest_foods(spicy_foods)
print_spicy_foods(spicy_foods)
get_spicy_food_by_cuisine(spicy_foods, "Thai")
get_average_heat_level(spicy_foods)
create_spicy_food(spicy_foods, spicy_food)