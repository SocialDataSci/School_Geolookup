import googlemaps

# read in API key
with open("api_key.txt", "r") as file:
    api_key = file.read()

# read in list of school names
# TODO this should be pointed to a view in the database

gmaps = googlemaps.Client(key=api_key)

# iterate through the list
# Geocoding and address
geocode_result = gmaps.geocode('General Mills Headquarters, MN')
print(geocode_result)

# take multiple column names
# combine them
# perform lookup
# perform join
# write out copy of data with geolocation
