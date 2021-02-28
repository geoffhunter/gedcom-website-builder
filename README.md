# gedcom-websitebuilder

Note: this utility needs the .py and .txt files in the gedcom-file-processor repository to function

This utility allows the user to produce HTML web pages, showing a family tree, from a GEDCOM format file.

An example is at https://familyhistoryrecords.000webhostapp.com/ 

It produces trees for up to 4 level-1 persons, e.g. the user’s grandparents. These level-1 persons are identified by their surname only, to protect their privacy in case they are still living. Other persons are shown with surname, forename(s) and year of birth. 

Where a person has associated documents, the name has a hyperlink to a documents index page, listing the documents, and each document name has a hyperlink to a page showing an image of the document.

Each tree page shows the level-1 person with their parents (level-2), grandparents (level-3) and great-grandparents (level-4), where known.

Where the level-4 person has known ancestors, a hyperlink is provided to take the user to the next level tree which starts with the level-4 person.

Each tree page has hyperlinks to the top-level of the other 3 trees. 

