- Make a visualisations of positon and magnitudes of objects. You can take a random sample from the available objects.
- PanSTARRS1 data archive home page[.](https://outerspace.stsci.edu/display/PANSTARRS)
- PS1 catalogue description page[.](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Source+extraction+and+catalogs)
	- PS1 Database object and detection tables[.](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Database+object+and+detection+tables)
- PS1 Mast CasJobs home page[.](http://mastweb.stsci.edu/ps1casjobs/)
- Notebooks example[.](https://ps1images.stsci.edu/ps1_dr2_query.html)

- **ObjectThin** Table contains positonal information for Objects in a number of coordinate systems
- **MeanObject** Contains the photometric information for objects based on single-epoch data, calculated as described in Magnier et al. 2013. 
- **MeanObjectView** Has all the essential object info, like position and magnitudes.

- **zMeanPSFMag** from PS1 MeanObject table
- **raStack** from PS1 ObjectThin table
- **decStack** from PS1 ObjectThin table
- **qualityFlag** from PS1 ObjectThin table  < 16 means good image.

- **fGetNearbyObjEq( ra, dec, radius in arc sec)** will return a table of all the objects in a radius mention within the ra and dec given.

#### PS1 catalogue

- The Extremely Luminous Quasar Survey in the Pan-STARRS 1 Footprint (PS-ELQS)([2019](https://iopscience.iop.org/article/10.3847/1538-4365/ab20d0)) 
	- Has a machine readable cds file that contains the PS1-ELQS footprint. 592 Quasars.

#### 2MASS and AII WISE catalogues

- The PS1 footprint is obtained by applying healpix on the 1,918,290 sources obained by matching the 2MASS and AII WISE JKW2 color cut satisfied sources to the PS1 sources.
- 2MASS and AII WISE data are stored in NASA/IPAC Infrared science archive[.](https://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-scan?submit=Select&projshort=WISE)
- 2MASS has j,k photometry, All WISE has W1, W2 photometry that we require.
- Catalog table name:
	- **fp_psc** - 2MASS Point Source Catalog
	- **allwise_p3as_psd** - AllWISE Source Catalog
	- `curl -o out.xml "https://irsa.ipac.caltech.edu/TAP/sync?QUERY=SELECT+*+FROM+TAP_SCHEMA.tables"` - To get all the table names and description.

> We use the 2MASS point source catalog (PSC), which was prematched to the _WISE_ AllWise source catalog.

\- Schindler et al. 2017

- Can be accessed from python via Astropy-affiliated Python package PyVO[.https://irsa.ipac.caltech.edu/docs/program_interface/astropy_TAP.html]

- **fGetNearestObjEq** inbuilt function that exist in the MAST casjobs is the key to our problem. Keyword - **Cursors and Table-valued Functions** . [See](https://galex.stsci.edu/casjobs/aqueries.aspx#cursors) 

