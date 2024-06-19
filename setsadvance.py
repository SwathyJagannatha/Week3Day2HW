#Python Sets Adventure
#Task 1: Flight Route Comparison** Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
# 1. Destinations that both airlines fly to. 
# 2. Destinations unique to your airline. 
# 3. Whether there are any destinations that neither airline shares.

def route_common(route1,route2):
    print("Common destinations that both airlines fly to:\n")
    print(route1.intersection(route2))
    pass

def route_unique(route1,route2):
    print("Unique destinations of our airline:\n")
    print(route1.difference(route2))
    pass

def route_unique_competitor(route1,route2):
    print("Unique destinations of our competitor airline:\n")
    print(route2.difference(route1))
    pass

def route_unique_both(route1,route2):
    print("Unique destinations of both the airline:\n")
    print(route2.symmetric_difference(route1))
    pass

def main(our_routes,competitor_routes):

    print("Destinations that both airlines have in common:")
    route_common(our_routes,competitor_routes)

    print("Destinations unique to our first airline(our_routes / route_one)\n")
    route_unique(our_routes,competitor_routes)

    print("Destinations unique to our second airline(competitor_routes / route_two)\n")
    route_unique_competitor(our_routes,competitor_routes)

    print("Destinations that neither airline shares\n")
    route_unique_both(our_routes,competitor_routes)
    pass

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

route_one = {"JFK","MAU","BAN","MAA","OAK","CDG"}
route_two = {"MAU","LSH","DXB","ANC","LAX","OAK"}

main(route_one,route_two)
#main(our_routes,competitor_routes)
