### White et al 2012

- 27129 redshift 2.2 < z < 2.8 quasars from SDSS BOSS.
- XDQSO algorithm used for target selection. Bovy et al. 2011
- angular completeness is tracked using MANGLE sectors.
- angular completeness is defined as the fraction of target quasars for which spectrum is obtained in each sector. Only survey areas with completeness 75% is considered.
- About spectroscopic completeness the discussion is quoted.
> We do not correct for spectroscopic incompleteness – i.e. account for the fraction of observed targets which produce a spectrum of sufficient quality to measure a redshift. Quasars at z > 2.2 are identifiable in BOSS even at very low signal-to-noise ratio because the strong Lyα λ1215 line always falls within the BOSS wavelength coverage (3600–10 000 Å; Eisenstein et al. 2011). In BOSS, almost all unidentifiable objects are likely to be stars, galaxies or low-redshift quasars, not the z > 2.2 quasars of interest in this paper. Correcting for spectroscopic incompleteness would induce a false large-scale clustering signal because the density of stellar contaminants varies over the sky.

### Powell et al. 2020

- Gaussian kernel smoothing is used to smooth out redshift distribution of data inorder to use it for drawing redshifts of random.

### Mountrichas et al 2016

- Small scale incompleteness due to slit collitions or finite number of science slit is model using methodology given in Hawkins et al. (2003).
- Technique focuses on weighting the pair counts to account for the incompleteness.
- Paper looks at the clustering of x-ray quasars from XMM-XXL survey with redshift provided mainly by SDSS.
- They measure the angular correlation function of target quasars and quasars with redshift available separately and compare it to see at what scale they deviate.
- Need to learn more about this.


### Hawkins et al. 2003

- Weighting schemes are used to correct for fibre collision effects.
- Each galaxy-galaxy pair is weighted with $$w_f = \frac{(1 + w_p)}{(1 + w_z)}$$
- where $w_p$ is the angular correlation function of the parent sample, and $w_z$ is the angular correlation function of the galaxies for which fibres are assigned and redshift is available. 
- For each galaxy-galaxy pair, along with redshift space distance and corresponding along and across the line of sight distances they also measure the angular separation and multiply with this factor to weight that pair in the sum.
- 



## Points
- We can determine the scale at which a particular factor in the clustering effects. For example the uncertainty in he footprint of the Shen quasars.

