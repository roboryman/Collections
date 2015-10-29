import sys
from prettytable import from_csv

# This file uses a third party library. PrettyTable: Display data in tables using a beautiful ASCII format.
# Thank you luke@maurits.id.au (code.google.com) for providing the prettytable library.

# TODO: Add filter functionality (ex. filter search engines with genre: google facebook duckduckgo -> google duckduckgo)

print "Run 'addCollection.py' to append Collection(s) to the Collections CSV file.\n"

collectionsData = open("Collections.csv", "r")
collectionsTable = from_csv(collectionsData)


def displayUnsorted():
  print collectionsTable
  collectionsData.close()
  x = raw_input("Press enter to exit.")
  sys.exit("Completed.")


def displaySorted():
  print "1. Sort by URL (default)"
  print "2. Sort by Genre"
  print "3. Sort by Description"
  print "4. Sort by Ranking"
  sortBy = raw_input("Select what you would like to sort by.")
  if sortBy == "1":
    print "Sorting by URL... This may take awhile."
    print collectionsTable.get_string(sortby='URL')
  elif sortBy == "2":
    print "Sorting by Genre... This may take awhile."
    print collectionsTable.get_string(sortby='Genre')
  elif sortBy == "3":
    print "Sorting by Description... This may take awhile."
    print collectionsTable.get_string(sortby='Description')
  elif sortBy == "4":
    print "Sorting by Ranking... This may take awhile."
    print collectionsTable.get_string(sortby='Ranking')
  else:
    print "Invalid input detected. Sorting by URL... This may take awhile."
    print collectionsTable.get_string(sortby='URL')

  collectionsData.close()
  x = raw_input("Press enter to exit.")
  sys.exit("Completed.")


sortQ = raw_input("Would you like to sort? (Y:y/N:n)")


if sortQ == "Y" or sortQ == "y":
  displaySorted()
elif sortQ == "N" or sortQ == "n":
  print "Displaying unsorted Collection (Original Order Sorting)...\n"
  displayUnsorted()
else:
  print "I'll take that as a no."
  print "Displaying unsorted Collection (Original Order Sorting)...\n"
  displayUnsorted()
