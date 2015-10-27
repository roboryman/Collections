import csv
import sys

# Collections: Add collection to Collections CSV db.
__author__ = 'Merrick Ryman'
# TODO: add remove/edit functionality

print "Use this script to append a collection."
print "Run 'Tables.py' to view Collections data in a readable format.\n"

f = open("Collections.csv", 'ab')


def addCollection():
    collectionURL = raw_input('Enter the URL for the new Collection: ')
    collectionGenre = raw_input('Enter the Genre for the new Collection: ')
    collectionDescription = raw_input('Enter the new Collection description: ')
    print "Appending to Collections..."
    writer = csv.writer(f)
    writer.writerow((collectionURL, collectionGenre, collectionDescription))
    print "Completed."
    continueOrNot()


def continueOrNot():
    choice = raw_input("Would you like to make another new collection? (Y/N)")
    if choice == "Y" or choice == "y":
        addCollection()
    elif choice == "N" or choice == "n":
        sys.exit("Completed.")
    else:
        print "I'll take that as a no."
        sys.exit("Completed.")


addCollection()
f.close()
