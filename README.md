# Collections [WIP]
Collections is ultimately designed to allow users to manage a custom domain index (with additional information).

As of right now, the system relies on a core CSV file (Collections.csv) to hold data. This may pose a problem; therefore everything is bound to be rewritten.

# TODO

- [ ] Master Collection
- [x] Add "popularity" column or ranking column
- [x] Sorting options (sort by URL, Genre, Description alphabetically, etc.)
- [ ] Filtering options
- [ ] Use custom ascii tables(really no need for this, the PrettyTables library is fine for this it seems)
- [ ] User ability to add/delete columns (URL, Genre, Description, etc.)
- [ ] Import from ranked lists (ex. Alexa)
- [x] Delete Collection(s)
- [x] Implement safeguard to prevent multiple entries of the same URL/ranking
- [x] Do not accept entries with an empty URL (re-ask?)
- [ ] Domain checker: checks if a domain is active using URL data from Collections (optional, user can turn on/off)

I am currently working on "Implement safeguard to prevent multiple entries of the same URL/ranking"


Feel free to commit some ideas if you want :-)
