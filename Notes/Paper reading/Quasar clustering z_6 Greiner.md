From the paper: Quasar clustering at redshift 6 ([2021](https://ui.adsabs.harvard.edu/abs/2021A%26A...654A..79G/abstract))

#### Questions
- What is $M_{1450}(AB)$? X-ray absolute magnitude.

#### Abstract and Introduction

#### Selection criteria, observations and data analysis

- 116 QSOs at $z = 5.6-6.6$ and $z$'-band brightness $=18.6-23.1$. Mainly from [Banados et al. (2016)](https://iopscience.iop.org/article/10.3847/0067-0049/227/1/11).
- GROND- Gamma ray burst optical/ near-infrared detector detects the afterglow of GRB in the optical and near infrared region.  used for observing 77 sources.
- GROND data is reduced using pyraf/IRAF.
- **We are looking for QSO companions?**

- GROND has g', r', i' ,z', J, H, $K_s$ bands.
- 
##### Color-Color selection of candidates
- Selection criterion:
	- i' - z' > 1.5 mag
	- z' - J > -0.7 mag
	- No detectios in g' and r' bands
- For z > 6.5
	- z' - J > -0.5 mag
	- J - H > -0.5 mag
	- no detection in i'

- This return 74 new high-z quasar candidates.
- 48 excluded through visual inspection.
- remaining 26 candidates shown in Fig. 2. as red dots.
- This criterion is satisfied by the initial QSOs all but 13. (upper limits in the i' - band)

- **Le PHARE** fit is done for 26 candidates inorder to distinguish late-type dwarfs from QSOs
	- steepness of the SED (Spectral energy distribution) in the i' - z' - J range
	- SED shape in the HK range which is much redder for dwarfs.

- **$A_V$** - Extinction, the reddening as a result of starlight traveling through dust grain.

- 2 SED is made one with $A_V$ correction (for Le phare fits with QSO) and one without (for Le phare fits with dwarfs. Because dwarfs in the current sensitivity range lies in a 100pc order and not significantly dust-effected.
- Out of 26
	- 14 is best fit with a dwarf.
	- 10 QSO at high z.      ---->Le phare fits on Fig. 6.
	- 1 galaxy at intermediate redshift
	- 1 not conclusive.
- Spectroscopy of 11 objects is obtained with GMOS instruments of the Gemini Observatory.

### Results and discussion
#### Pair candidates
- No QSO pair candidate brighter than $M_{1450}(AB) < -26$ mag in our GROND data of 116 QSOs
- But color selection and SED fitting recovered QSOs reported by Banados with only 5% mismatch.
- Empirically they expect 3 pairs in the sample. 1 every 40 QSOs or 2.5%.
	- Assumes that the quasar clustering fraction does not evolve with redshift.
	- Makes laws after discovery!!??
	- Ignored different luminosity ranges sampled at different redshifts.
- From Kulkarni et. al. (2019) they get number density $9\times 10^{-10}Mpc^{-3}$ for quasars with $M_{1450} < -26$ mag for redshift range $5.6 < z < 6.6$. 
- $\rightarrow$ upper limit of $w_p < 110 000 h^{-1}Mpc$. Fig. 3. 
- $\rightarrow$ autocorrelation length $r_0 < 1000h^{-1}Mpc$.

#### Completeness and biases
- Two questions arise
1. whether selection criteria which discovered the original quasars have some bias against binary quasars?
	- Potential bias is that the seeing limit in the original survey data affects the discovery of QSO on 1-2'' scales due to nearby contaminating sources. Since this is statistical, not expected to affect the fraction of binary QSOs in the spectroscopically confirmed QSO sample.
2. Whether the current search strategy misses QSO?
	1. What is the completeness of color-color cuts?
		- Tested with the confirmed sources and incompleteness is about 5%
	2. What is the completness of Le PHARE fits in recognizing QSOs
		- Again tested on the known quasars and incompleteness is $<5$%.

#### Conclusion
- No candidate QSO pair is found in the search of 116 spectroscopically confirmed redshift 6 quasars.
	- within 0.1 - 3.3 $h^{-1}cMpc$ search radius
	- companion brighter than $M_{1450}(AB) < -26$ mag.
- Consistent with cosmological large-scale galaxy evolution simulations. ILLUSTRIS-TNG300, L-GALAXIES 2020, MASSIVEBLACK-II, BLUETIDES.
- Inconsistent with the serendipitous discovery of QSO pairs at z = 4.26 and z = 5.02, suggesting one pair every 40 QSOs, or 2.5%.
- No claims are made that clustering at redshift 6 is less than that of redshift 5, due to low statistics and uncertainities of the serendipitous discoveries.
