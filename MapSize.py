import os

print "The downloaded file is {} MB".format(os.path.getsize('map')/1.0e6)
print "The JSON file is {} MB".format(os.path.getsize('map.json')/1.0e6)
