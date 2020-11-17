from collections import OrderedDict

def main():

    # dict definitions
    cities_zip = dict()
    cities_zip_ordered = OrderedDict()

    # code to read file
    with open('cities.csv') as f:
        for line in f:
            cities_list = line.strip("\n").split(",")

            # Todo 1: Add the cities and their zip codes to both dictionaries

            location = cities_list[0]
            zip_code = cities_list[1]

            cities_zip[location] = zip_code
            cities_zip_ordered[location] = zip_code
            
    # Todo 2: Add code here to iterate over both dictionaries
    for location, zip_code in cities_zip.items():
        print(location, zip_code)

    print("\n\n")
    for location, zip_code in cities_zip_ordered.items():
        print(location, zip_code)
            
if __name__ == "__main__":
   main()
