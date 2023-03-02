- From the [paper](https://ui.adsabs.harvard.edu/abs/2017JCAP...07..017L/abstract)

### Questions
- Are they not finding the completeness of the selection process from target to observed? not targeting process itself!!

### Introduction
- Influence of baryons on galaxy clustering.
- Baryon driver fluctuation in matter power spectrum as a standard ruler.
- 2df QSO redshfit survey.
- This paper is going to focus on systematic errors in clustering measurement. Include contamination by stars, forground etc.
- Weighting maps and exclusion masks as remedies.
- Sample contains 70,000 optically luminous quasars in the redshift range 0.9 < z < 2.2.

### Data Sample
##### eBoss survey
- Six years from July 2014. 
- estimated sample of more than 500,000 confirmed quasars
	- 7500 $deg^2$
	- $0.9 < z < 2.2$
	- Allow for measurement of BAO scale, angular diameter distance $d_A(z)$, and $H(z)$.

##### Quasar selection
- Homogeneous CORE selection, combines
	- selection in (u, g, r, i, z) using a likelihood-based routine calles **XDQSOz**
	- mid-IR-optical color cut
- Another quasar selection is also there dedicated to $z>2.2$ Lyman-$\alpha$ quasars, with an average of 20 targets per $deg^2$.
- In contrast to quasars, stars tends to be dim in the mid-IR wavelengths.
- $m_{opt} - m_{IR} \geq (g - i) + 3$, reduces star contamination in our sample without significantly removing quasars.
- selection results in average 115 targets per $deg^2$.
	- 25 already observed by SDSS I, II, III
	- 13 out of 25 "known quasars" and 58 out of 90 "eBOSS quasars".
	- Thus 70 quasars per $deg^2$ reach 2% accuracy on the BAO scale.?
- part of eBOSS footprint was observed by SEQUELS. Has some differences with eBOSS.
- Data used in the paper consists of first year of eBOSS data. 1200 $deg^2$. 

##### SDSS spectrograph
- Aluminium plate set at the focal plane of the telescope with $3^o$ diameter field-of-view.
- Holes drilled in the plate corresponding to 1000 targets.
- Optical fibre is plugged to each holes and links to the spectrographs.
- Minimum distance between two fibres on the same plate corresponds to 62'' on the sky.
- But there are overlapping plates too.

### Analysis
##### Computing $\xi(r)$ 
- Limited number of fibers are there, so all targets cannot be observed.
- Density of eBOSS targets is not homogeneous, therefore probability to observe is not homogeneous.
- Targets are more likely to be observed where plates overlap.
- Defines polygons at the intersections of the plates projected on the celestial sphere.
- Completeness is defined in each polygon as, $$C = \frac{N_{obs} + N_{col}}{N_{targets} - N_{known}}$$
	- $N_{obs}$ - number of observed targets. 
	- $N_{targets}$ - total number of targets. 
	- $N_{known}$ - number of targets that have already been observed by the SDSS I, II and BOSS surveys.
	- $N_{col}$ - number of targets that were not observed because they are colliding with another quasar.
- $N_{known}$ appears with minus sign in the dinominator because the completeness of known targets is 1 by definition and adding it will skew the completeness of the unknown targets.
- $N_{col}$ appears in the numerator inorder to account for the fact that when we decide to observe a target, the probability of observing the colliding targets goes to zero by default. It is a limitation in the design.
- They also include the known targets in their analysis, but only with a selection probabilty proportional to the completeness of the polygon.
- Using this completeness a 'catalog of $10^7$ object with 'random' angular position is made with number of objects in each polygon proportional to the area and completeness of the polylgon.
- Each random object is then assigned a redshift drawn from the distribution $n(z)$.
- Then correlation is calculated from Landy-Szalay estimator.

##### Estimation of Statistical uncertainitly
- Covariance matrix of correlation function is found from the bootstrap resampling method.
- Each galactic cap is partitioned into 201 bootstrap cells.
- 201 cells is drawn with replacement from these partitioning to get a bootstrap realisation.
- $\xi(r)$ is measured from each of the 10,000 realisations, and covariance matrix is calculated.
- Covariance matrix is also found from 100 QPM (Quick Particle Mesh is an Nbody simulation for large-scale structure of the universe) mocks.
- These mocks are inaccurate at smaller scales.
- Fig. 3. and 4. gives the covariance matrix and their comparisons.

### Systematic effects
##### Inhomogeneities of target identification
- Efficiency of target identification is better for visual inspection than pipeline.
- Efficiency depends on the signal to ration, which inturn depends on the positioning of the fibre. $n_{ID}$
- Fibres at the edge ($n_{ID}$ near 0, 500, 1000) have less S/N ration.
- Fig. 5. shows this effect.
- Effect can be modeled using hyperbolic cosine with 3 free parameters, $$ \frac{N_{QSO}}{N_{fibres}}(n_{ID}) = -a \cosh \left(\frac{n_{ID} \hspace{0.1cm}\text{mod}\hspace{0.1cm} 500 - 250}{b}\right)^2 + c$$
- Inverse of this is used as a weight for the new eBOSS quasars. For known quasars for which this is not available, inverse of mean is used, to account for difference in efficiency.

#### Inhomogeneities of quasar target selection
- Variations of observed quasar density with depth and its inputs (seeing, airmass, extinction and sky-flux) and also with sky density (blending effect) is shown in Fig. 6.
- Healpix map for the above quantity is generated with $N_{side} = 256$. As per procedure of [Ross et al. 2012].
- Ratio of number of observed quasars to the normalized number of random objects is proportional to the observed quasar density corrected for the completness.
- No bias in the target selection due to blending is seen.
- Final systematic weights for target selection inhomogeneity are obtained by multiplying the depth and Galactic-extinction weights.

##### Effect of weightings on $\xi(r)$
- Fig. 7 shows the effect of various weights for correcting systematic effects.
- cross-$\chi^2$ between $\xi_N(r)$ and $\xi_S(r)$ (NGC and SGC)$$\chi_{NS}^2 = \sum_{ij}(\xi_N(r_i) - \xi_S(r_i))C_{ij}^{-1}(\xi_N(r_j) - \xi_S(r_j))$$where C is the sum of $C_N$ and $C_S$, the covariance matrices of $\xi_N(r)$ and $\xi_S(r)$. Table. 1 shows the result for various weighting schemes.

##### Measurement of quasar bias
- From flat $\Lambda$CDM model, with parameter same as BOSS 12th data release, CAMB and HALOFIT provide a non-linear matter power spectrum $P_{mat}(k)$. 
- Linear redshift distortion accounted for using the Kaiser formula.
- $$P_Q(k,\mu) = b_Q^2(1 + \beta \mu_k^2)^2 P_{mat}(k)$$$\mu_k$ is the cosine of the angle between $k$ and the line of sight, $\beta = f/b_Q$, and $f\simeq \Omega_m^{0.55}(z)$ is the growth rate of structure.
- Now $P_Q(k)$ is converted into $\xi_Q(r)$.
- Fits of $b_Q$ are performed using the MINUIT libraries over the range $10 < r < 85h^{-1}Mpc$.
- $$\xi_{QSO}(s)/\xi_{mat}(r) = b_Q^2(1 + \frac{2}{3}\beta + \frac{1}{5}\beta)$$where we have used $\xi(s) = \xi(r)(1 + \frac{2}{3}\beta + \frac{1}{5}\beta)$ from [Kaiser 1987].
- Measurement of $b_Q$ are not sensitive to the range of the fit. Fig. 8.
- $b_Q(z) = \alpha[(1+z)^2 - 6.565)] + \beta$, empirical formual obtained from [Croom et al. 2005]. $\alpha = 0.278 \pm 0.018$, $\beta = 2.393 \pm 0.042$ and $\rho_{\alpha,\beta} = 0$.

##### Characteristic Halo Mass
- $\bar M_h$ is the characteristic halo mass that corresponds to the measured clustering bias, $b(\bar M_h) = b_Q$
- Fig. 10 shows the characteristic and minimum halo masses, for full sample and subsamples with redshift.
- $M_{h,min}$ is the minimum halo mass that bounds the range of haloes that correspond to the observed clustering bias, $$b(M > M_{h,min}) \equiv \frac{\int_{M_{h,min}}^\infty \frac{dn}{dM}b(M)dM}{\int_{M_{h,min}}^\infty \frac{dn}{dM} dM}$$where $\frac{dn}{dM}$ is the halo abundance determined by Tinker et al. 2008. 
- How quasar clustering varies with luminosity appears to be a subtle effect.
- Confidence interval in Fig. 10 is obtained from a projection from confidence interval of $b_Q$ at average redshift to halo masses via the above equation.
- Possibility of a sharp change in host halo mass of low and high reshift quasars.
- Constant bias with redshift causes the characteristic mass of the average halo to dwindle (current work), and increasing bias causes the characteristic mass to be constant ([Eftekharzadeh et al.] seen in Fig. 10).
- Structure has had less time to grow at higher redshift, hence increasing bias will offset this.

##### Duty cycle
- $$f_{duty} = \frac{\int_{L_{min}}^{L_{max}}\Phi(L)dL}{\int_{M_{h,min}}^\infty \frac{dn}{dM}dM}$$
- Since we are integrating over all masses from $M_{h,min}$ to $\infty$, we implicitly assume extremely weak relationship between halo mass and luminosity.
- QLF adopted from [Palanque-Delabrouille et al. 2016]
- Error on $f_{duty}$ is calculated by taking the quasar bias from a Gaussian corresponding to the 68% confidence interval around our measured $\pm 1\sigma$ errors on $b_Q$ and find the implied $\pm 1\sigma$ error in $f_{duty}$. Fig. 11.
- 


### Conclusion
- Main contribution to systematics is the **inhomogeneities in the target selection**.
- Provides weighting scheme?
- Measured correlation function agrees with the $\Lambda$cdm model in the range $10 < r < 85 h^{-1}Mpc$.
- Measured values:
	- Quasar bias, $b_Q = 2.45 \pm 0.05$, at $\bar z = 1.55$.
- $b_Q$ increases with $z$ in the studied redshift range.
- [Tinker et al. 2010] is adopted to calculate minimum halo mass, $M_{h,min}$, and the characteristic halo mass, $\bar M_h$.
- Assumed luminosity independence of the quasar clustering.
- Characteristic mass of haloes hosting quasars remains relatively constant at $z < 2.2$. (Agreement with [Croom et al. 2005, Eftekharzadeh et al. 2015])
- Duty cycle of eBOSS quasars at $\bar z \sim 1.5$ is more than four times longer than that of BOSS quasars at $\bar z \sim 2.5$.
- Fewer quasars are "on" at $z \sim 2-3$ is proposed as an explanation for reducing duty cycle.
- eBOSS quasars at $0.9 < z < 1.2$ in their sample is $2-3$ times less than that at $1.5 < z < 1.8$ and have smaller $M_{h,min}$.
- Nevertheless clustering signal is dominated by rare most massive haloes.
- Luminosity dependence will be investigated with the final sample $\sim 500,000$ eBOSS quasars.

