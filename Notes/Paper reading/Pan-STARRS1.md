- Notes mainly from [here](https://en.wikipedia.org/wiki/Pan-STARRS)
- Panoramic Survey Telescope and Rapid Response System
- Astronomical cameras, telescopes and a computing facility
- Surveys the sky for moving or variable objects on a continual basis
- Outputs accurate astrometry and photometry
- Primary mission now is to detect Near-Earth Objects that threaten impact events
- Expected to create a database of all objects visible from Hawaii (three-quarters of the entire sky) down to apparent magnitude 24.
- $2010 - 2014$

### Instruments

- Two $1.8m$ Ritchey-Chretien telescopes (RC is used in Hubble, Keck etc.)
- Largest digital camera ever built. (A 1.4 Gigapixel camera)
- Analysis pipeline by Gene Magnier
- Nick Kaiser is the PI of the Pan-STARRS project.
- Due to some technical difficulties, PS1 images are slightly less sharp that initially planned.
- Requires:
	- 2GB storage per image
	- $30-60$ seconds exposure (enough for $m = 22$)
	- Additional $1 min$ for computer processing
	- 10TB data every night
- $\sim 6000deg^2$ sky can be imaged every night. (Entire sky is $41,253.0 deg^2$ of which $30,000deg^2$ is visible from Hawaii)
- Area equivalent to entire sky can be surveyed four times a month.
- Imaged sky 12 times in initial 3 year mission in each of 5 filters

### Filters

- Filters $g$, $r$, $i$, $z$, $y$. 
- Filters $g$, $r$, and $i$ have the same bandpasses of SDSS. Midpoints and FWHM:
	- $g$ - 464 *nm* and 128 *nm*
	- $r$ - 658 *nm* and 138 *nm*
	- $i$ - 806 *nm* and 149 *nm*
- $z$ filter has the SDSS midpoint (900 *nm*), but longwave cutoff avoids water absorptions bands beginning at 930 *nm*.
- Shortwave cutoff of the $y$ filter is set by the water absorption bands that end around 960 *nm*. Longwave cutoff band in currently at 1030 *nm* to avoid the worst of the detector sensitivity to temperature variations.

### Science

- Data collection started early in 2010 and completed in April 2014.
- Works in complement with WISE orbital telescope.


### Data access

- Data releases:-
	- PS1 DR1 - Dec 19, 2016
	- PS1 DR2 - Jan 28, 2019
- Data from PS1 are archived at the Space Telescope Science Institute (STScI) in Baltimore Maryland. [Pan-STARRS1 data archive home page](https://outerspace.stsci.edu/display/PANSTARRS/Pan-STARRS1+data+archive+home+page).
- Can be accessed through MAST, the [Mikulsky Archive for Space Telescopes](https://archive.stsci.edu/missions-and-data/pan-starrs).
- Additional support for the PS1 public science archive is provided by the [Gordon and Betty Moore Foundation](https://www.moore.org/).
- Papers describing the instrument, survey and data analysis:
	- [PS1 Surveys](https://arxiv.org/abs/1612.05560), Chambers, K.C., et al.
	- [PS1 Data Processing](https://arxiv.org/abs/1612.05240), Magnier, E. A., et al.
	- [PS1 Pixel Processing](https://arxiv.org/abs/1612.05245), Waters, C. Z., et al.
	- [PS1 Source Detection](https://arxiv.org/abs/1612.05244), Magnier, E. A., et al.
	- [PS1 Calibration](https://arxiv.org/abs/1612.05242), Magnier, E. A., et al.
	- [PS1 Database](https://arxiv.org/abs/1612.05243), Flewelling, H. A., et al.
- [How to retrieve and use PS1 data](https://outerspace.stsci.edu/display/PANSTARRS/How+to+retrieve+and+use+PS1+data)?

- There is an Internal data release. Look Benados et al (2016)

### Questions

- on-going or not?
- why nobody is looking at quasar clustering in PS1?
- What is Pan-STARRS2?

### Goals

- To understand how PS1 stores data. **Structure**
- Understand how to retrieve data **Efficiently**
- 