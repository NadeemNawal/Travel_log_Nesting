# Nesting dictionary inside a list
travel_log=[
{
    "country":"Germany", 
    "visits" : 12, 
    "cities": ["Berlin",   "Hamburg", "Stuttgart"]
},
{
  "country":"France", 
  "visits" : 12, "cities": ["Paris", "Nice","Monte Carlo"]
}
]
# print(travel_log)
country=input("What country did you visit? ")
visits=int(input("How many times did you visit the city? "))
list_of_cities= input("What cities did you visit? ").split()

def add_country(name, times_visited, cities_visited):
    new_country={}
    new_country["country"]=name
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
   
add_country(name=country, times_visited=visits, cities_visited=list_of_cities)
print(travel_log)
