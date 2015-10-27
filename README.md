# Collections [Major WIP]
Collections is ultimately designed to allow users to manage a custom domain index (with additional information).

As of right now, the system relies on a core CSV file (Collections.csv) to hold Collections data. This may pose a problem with very large Collections; therefore everything is bound to be rewritten.

The current columns are: "URL", "Genre", and "Description".
I plan to add much farther functionality in the future. Right now, Collections really doesn't do much. Here are some of the ideas I have had so far:

- Master Collection
- Sorting options (sort by URL, Genre, Description alphabetically, etc.)
- Filtering options
- Use custom ascii tables(really no need for this, the PrettyTables library is fine for this it seems)
- User ability to add/delete columns (URL, Genre, Description, etc.)

Feel free to commit some ideas if you want :)
