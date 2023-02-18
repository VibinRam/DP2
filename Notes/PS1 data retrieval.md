- Make a visualisations of positon and magnitudes of objects. You can take a random sample from the available objects.
- PanSTARRS1 data archive home page[.](https://outerspace.stsci.edu/display/PANSTARRS)
- PS1 catalogue description page[.](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Source+extraction+and+catalogs)
	- PS1 Database object and detection tables[.](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Database+object+and+detection+tables)
- PS1 Mast CasJobs home page[.](http://mastweb.stsci.edu/ps1casjobs/)

- **ObjectThin** Table contains positonal information for Objects in a number of coordinate systems
- **MeanObject** Contains the photometric information for objects based on single-epoch data, calculated as described in Magnier et al. 2013. 
- **MeanObjectView** Has all the essential object info, like position and magnitudes.

- **zMeanPSFMag** from PS1 MeanObject table
- **raStack** from PS1 ObjectThin table
- **decStack** from PS1 ObjectThin table
- **qualityFlag** from PS1 ObjectThin table  < 16 means good image.

- **fGetNearbyObjEq( ra, dec, radius in arc sec)** will return a table of all the objects in a radius mention within the ra and dec given.