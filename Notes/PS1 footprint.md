![[apjsab20d0f1_lr.jpg]]
- Footprint is essentially the effective area of the sky included in the survey. It depends on the imaging survey geometry, missing data, existence of very bright stars and so on. Jiang et al. 2016 (sec 4.2). 
- An example of footprint is shown in grey in the above image.

##### HEALPix

- Schindler et al. 2019 has a section on PS1-ELQS footprint, which refers to two papers (HEALPix; Gorski et al 2005) and Jiang et al. (2016).

- HEALPix is a Hierarchical Equal Area, and IsoLatitude Pixelisation of the sphere. Basically it pixelates the sphere.![[Pasted image 20230221173137.png]]

- Coordinate system used for mollewide in healpy : Standard coordinates are the colatitude $\theta$, 0 at the North Pole, $\pi/2$ at the equator and $\pi$ at the South Pole and the longitude $\phi$ between 0 and $2\pi$ eastward, in a Mollview projection, $\phi = 0$ is at the center and increases toward the left of the map.

- In level 0, the sphere is devided into 12 pixels of equal area. In the subsequent levels this goes as $N_{pixels} = 12 \times 4^{lvl}$.
- In healpy, the parameter determining the number of pixels and thereby resolution is $N_{side}$. And $N_{side} = 2^{lvl}$.

```python
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
- Schindler et al. 2019 uses 1,918,290 sources selected from their photometric JKW2 color cut to estimate the coverage area.