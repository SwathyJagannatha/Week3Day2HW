#Task 1: Formatting Flight Itineraries 

def format_itinery(flight,cnt):
    for name in flight:
        print(f"Itinerary {cnt+1} : {name[0]} - From {name[1]} to {name[2]}")
        cnt = cnt + 1
    pass

def main(flight):
    print("Flight Itinery details:")
    cnt=0
    format_itinery(flight,cnt)
    # print("Aditional itineries:")
    # format_itinery(itinery_1,cnt)

flight=(("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"))
itinery_1 = (("Jenny","San Jose","Honolulu"),("Bryer","Maui","Canada"))
main(flight)
