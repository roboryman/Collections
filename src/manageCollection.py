import csv
import sys
import os

# Collections: Add/remove collections to Collections CSV

print "Use this script to append/remove collection(s)."
print "Run 'Tables.py' to view Collections in an easily readable format.\n"


def removeCollection():
    remCollectionsIn = open('Collections.csv', 'rb')
    remCollectionsOut = open('Collections-temp.csv', 'wb')
    located = False
    deleteCollection = raw_input('Enter the URL of the collection you wish to remove: ')
    if deleteCollection == 'URL':
        print "Stop trying to break the program you cheeky scrub. Lets try that again.\n"
        removeCollection()
        
    csvreader = csv.reader(remCollectionsIn, dialect='excel-tab')
    csvwriter = csv.writer(remCollectionsOut, dialect='excel-tab')
    for row in csvreader:
        if row[0] == deleteCollection:
            located = True
            continue
        else:
            csvwriter.writerow(row)
            continue
    
    remCollectionsIn.close()
    remCollectionsOut.close()
    os.remove('Collections.csv')
    os.rename('Collections-temp.csv', 'Collections.csv')
    
    if located == False:
        removeChoice = raw_input('Failed to find the specified URL. Try Again? (Y:y/N:n): ')
        if removeChoice == "Y" or removeChoice == "y":
            removeCollection()
        elif removeChoice == "N" or removeChoice == "n":
            continueOrNot()
        else:
            continueOrNot()
    elif located == True:
        print "Completed.\n"
        continueOrNot()
    else:
        sys.exit("I honestly have no idea how this would happen.")


def addCollection():
    global collectionURL
    collectionURL = raw_input('Enter the URL for the new Collection: ')
    collectionURL = questionMark(collectionURL)
    collectionGenre = raw_input('Enter the Genre for the new Collection: ')
    collectionGenre = questionMark(collectionGenre)
    collectionDescription = raw_input('Enter the new Collection description: ')
    collectionDescription = questionMark(collectionDescription)
    collectionRanking = raw_input('Enter the global ranking number if you know it (optional): ')
    collectionRanking = questionMark(collectionRanking)
    
    print "Appending to Collections...\n"
    with open('Collections.csv', 'ab') as collectionsFile:
        writer = csv.writer(collectionsFile, dialect='excel-tab')
        writer.writerow((collectionURL, collectionGenre, collectionDescription, collectionRanking))
    print "Completed."
    continueOrNot()


def questionMark(collectionVariable):
    if not collectionURL:
        print "You must enter a URL.\n"
        addCollection()
    else:
        if not collectionVariable:
            collectionVariable = 'N/A'
            return collectionVariable
        else:
            with open('Collections.csv', 'rb') as collectionsFile:
                reader = csv.reader(collectionsFile, dialect='excel-tab')
                for row in reader:
                    if row[0] != collectionURL:
                        pass
                    else:
                        print "That URL already has an entry. Try again.\n"
                        addCollection()
    return collectionVariable


def continueOrNot():
    choice = raw_input("Would you like to append or delete another collection? (Y:y/N:n): ")
    if choice == "Y" or choice == "y":
        begin()
    elif choice == "N" or choice == "n":
        sys.exit("Completed.")
    else:
        print "I'll take that as a no."
        sys.exit("Completed.")


def begin():
    print "1. Append a new Collection"
    print "2. Remove an existing Collection"
    print "3. Exit"
    choice = raw_input("Please select what you would like to do: ")
    if choice == "1":
        addCollection()
    elif choice == "2":
        removeCollection()
    elif choice == "3":
        print "Exiting..."
        sys.exit("Completed.")
    else:
        print "Ill take that as an exit..."
        sys.exit("Completed.")


begin()
