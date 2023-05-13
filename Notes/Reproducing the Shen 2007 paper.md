- Sample selection:
	- The quasars observed through the third data release have been logged cataloged by [Schneider et al 2005]
	- [Schneider et al 2006] extends the catalog to DR5
	- Paper only looks for clustering on larger scales. Smaller scales on a future paper?
	- Have taken all quasars from SDSS quasar catalog with $z \geq 2.9$. (3333 in total)
	- 2,805 quasars added to the sample from plates taken since DR3.
	- Final sample of 6,109 after rejecting 29 from the above.
- Subsample selection:
	- Only 4,426 quasars in total.

- How to make random catalog is given here[.](https://arxiv.org/pdf/1712.03128.pdf)
	-  We can take data catalog with 100 times more data points than the signal catalog. Normalisation is necessary in the estimator.
	- They have only about 1000 quasars in their catalog.
	- MANGLE software to create the mask of the region containing quasars. random catalog is made in this mask.
	- They are also combining the survey geometries of more than one surveys.
- How to divide the survey geometry into equal area regions for jackknife sampling is given here[.](https://ui.adsabs.harvard.edu/abs/2021MNRAS.501.3309Z/abstract)
	-  Code given here[.](https://github.com/rongpu/pixel_partition)

### Making random catalog
- A random catalog is made using healpy.
- **Choosing the appropriate HealPix level**: Effective coverage area of all the SDSS quasars is made for different levels. Appropriate level for the analysis is chosen by looking at the sudden fall off in area.
- **Increase the map resolution**: Increase the number of pixels in the effective survey area by upscaling the resolution of the HealPix map.
- **Random pixels are selected**: Random pixels are selected from this high resolution map, in order to assign the random sources.
- **Converted the random pixels to a random ra and dec**: This gives the random catalog.

### Selection function from Richards et al 2006
- Throughout this paper we use a  cosmology with m ¼  
0:3,  ¼ 0:7, a Hubble constant of H0 ¼ 70 km s1 Mpc1  
(e.g., Spergel et al. 2003), and luminosity distances determined  
according to Hogg (1999) for this cosmology.
- 

