- Ref [Schindler et al 2019](https://iopscience.iop.org/article/10.3847/1538-4365/ab20d0) , [Jiang et al. 2016](https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222)


![[apjsab20d0f1_lr.jpg]]
- Footprint is essentially the effective area of the sky included in the survey. It depends on the imaging survey geometry, missing data, existence of very bright stars and so on. Jiang et al. 2016 (sec 4.2). 
- SDSS ELQS footprint is shown in grey in the above image.

##### HEALPix

- Schindler et al. 2019 has a section on PS1-ELQS footprint, which refers to two papers (HEALPix; Gorski et al 2005) and Jiang et al. (2016).

- HEALPix is a Hierarchical Equal Area, and IsoLatitude Pixelisation of the sphere. Basically it pixelates the sphere.
- ![[Pasted image 20230221173137.png]]

- **healpy** is a python implementation of HEALPix library.
- There is another implementation associated with astropy, **astropy_healpix**

- Coordinate system used for mollewide in healpy : Standard coordinates are the colatitude $\theta$, 0 at the North Pole, $\pi/2$ at the equator and $\pi$ at the South Pole and the longitude $\phi$ between 0 and $2\pi$ eastward, in a Mollview projection, $\phi = 0$ is at the center and increases toward the left of the map.

- In level 0, the sphere is devided into 12 pixels of equal area. In the subsequent levels this goes as $N_{pixels} = 12 \times 4^{lvl}$.
- In healpy, the parameter determining the number of pixels and thereby resolution is $N_{side}$. And $N_{side} = 2^{lvl}$.

```python
import numpy as np
import healpy as hp

level = 6

nside = 2 ** level

  

ra_values = np.radians(schind_data.columns[1])

dec_values = np.absolute(np.radians(schind_data.columns[2]) - np.pi/2)

  

pixel_indices = hp.ang2pix(nside, dec_values, ra_values)

  

npixels = hp.nside2npix(nside)

all_pixels = np.zeros(npixels)

all_pixels[pixel_indices] = 1

  

hp.mollview(all_pixels)
```

- `ang2pix` - return the pixel, the angle is included in.
- `nside2npix` - returns the number of pixels from nside.
- `mollview` - plots a molleweide projection of the pixels.

![[Pasted image 20230221172656.png]]pixels corresponding to PS1-ELQS quasars. Level = 6. 

- Footprint or effective area is calculated from the area covered by pixels that contains data points.
- Schindler et al. 2019 uses 1,918,290 sources selected from their photometric JKW2 color cut to estimate the coverage area (footprint of quasars). lvl = 6 of $N_{pix} = 196,608$ (a missmatch of ground level is there) is adopted in the paper.

- We need to find the sweatspot for the HEALPix resolution. Lower resolution won't be able to pick out the fine structure of galactic extinction map, higher resolution will introduce statistical fluctuations into the effective area measurement.

#### Footprint of $z > 5.6$ quasars
- [Schindler et al 2023] uses 328, 479, 702 sources of the PS1 PV2 catalog, which passed the photometric quality criteria and the morphology selection, and were included in the area defined by the extinction selection and the Galactic plane and M31 exclusion regions.
- HEALPix lvl 10 is used, with estimated survey area $= 20803.38^{+61.75}_{-54.45} deg^2$.
- ![[Pasted image 20230317150641.png|500]]
