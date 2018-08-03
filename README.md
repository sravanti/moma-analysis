# MoMA Collection DB Analysis

This repository is to support analysis of the Museum of Modern Art's collection metadata. 
This includes: 
- `artoveryear.py` — an analysis of gender and nationalities over time
- `analysis.py `— assorted functions that I used in my prior analysis of the MoMA repo (but have not actively used for a few years)
- `momadb.db`—my slightly modified database built from the CSV files MoMA provides. Modifications include correcting for case in gender (e.g. "Male" and "male" have been condensed to "Male") and a couple of mistyped years have been corrected.

Note that the SQL database includes a table of American female artists represented in the dataset with ethnicity information. This was pulled from the [NamSor Diaspora API](https://api.namsor.com/namsor/faces/viewapikey.xhtml). 

The information provided has not been endorsed by MoMA and information from the original data set has been modified. Use of this database is available without restriction.
