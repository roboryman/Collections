import sys
from prettytable import from_csv

# This file uses a third party library. PrettyTable: Display data in tables using a beautiful ASCII format.
# Thank you luke@maurits.id.au (code.google.com) for providing the prettytable library.

# TODO: Add sort functionality (ex. sort by URL or genre by alphabetical order)

print "Run 'addCollection.py' to append Collection(s) to the Collections CSV file.\n"

collectionsData = open("Collections.csv", "r")
collectionsTable = from_csv(collectionsData)


def displayUnsorted():
  print collectionsTable
  collectionsData.close()
  x = raw_input("Press enter to exit.")
  sys.exit("Completed.")


def displaySorted():
  print "1. Sort by URL"
  print "2. Sort by Genre"
  print "3. Sort by Description"
  sortBy = raw_input("Select what you would like to sort by.")
  if sortBy == "1":
    print collectionsTable.get_string(sortby='URL')
  if sortBy == "2":
    print collectionsTable.get_string(sortby='Genre')
  if sortBy == "3":
    print collectionsTable.get_string(sortby='Description')
  collectionsData.close()
  x = raw_input("Press enter to exit.")
  sys.exit("Completed.")


sortQ = raw_input("Would you like to sort? (Yy/Nn)")

if sortQ == "Y" or sortQ == "y":
  displaySorted()
elif sortQ == "N" or sortQ == "n":
  print "Displaying unsorted Collection... This may take awhile.\n"
  displayUnsorted()
else:
  print "I'll take that as a no."
  print "Displaying unsorted Collection... This may take awhile.\n"
  displayUnsorted()
