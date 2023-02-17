- [From these notes](https://ned.ipac.caltech.edu/level5/March12/Coil/)

#### 1. Historical background

- On angular scales less than $10^o$, deviation from poisson distribution ~ [Hubble(1934)]
- Angular 2 point correlation function follows roughly a power law distribution over angular scales of ~ $0.1^o - 5^o$. ~ [Peebles(1975) ]from Lick galaxy catalogue.

#### 2. The two-point correlation function

- $\xi(r)$ is defines as a measure of the excess probability $dP$, above unclustered random Poisson distribution. $$dP = n[1 + \xi(r)]dV$$
- **Note:** What will be random poissonian distribution?
	- If we partition the universe into grids of equal volume, the number of quasars in each grid will be poisson distributed. If you make a histogram of number of quasars v/s frequency of occurance that number, that will follow of poisson curve.
- Fourier transform of the two point correlation function is the [[power spectrum]]. Several different estimators for $\xi(r)$ have been proposed and tested
- [Davis & Peebles(1983)]$$\xi = \frac{n_R}{n_D}\frac{DD}{DR} - 1$$
- [Hamilton(1993)]$$\xi = \frac{DD\:RR}{(DR)^2} - 1$$
- Most commonly used, [Landy & Szalay(1993)]$$\xi = \frac{1}{RR}\left[DD \left(\frac{n_R}{n_D}\right)^2 - 2DR\left(\frac{n_R}{n_D}\right) + RR\right]$$
- where $D$ is the Data catalogue and $R$ is the random catalogue. $DD$ is the counts of pairs of galaxies in bins of seperation. $n_R$ and $n_D$ are mean number densities of galaxies in the data and random catalogue.

#### 3. Angular clustering

- To determine the 3 dimensional correlation function, we require the knowledge of the redhsifts of the galaxies. This is a difficult data to obtain for a large fraction of galaxies. Angular clustering measurements are done where redshift data is not available. Interpretation of angular clustering results can be unreliable due to degenerecies between clustering amplitude and redshift contributions.
- 2d projected angualar correlation function $w(\theta)$, $$dP = N[1 + w(\theta)]d\Omega$$
- Generally be fit with a power law, $$w(\theta) = A_w\theta^\delta$$
- 

#### 4. Real and redshift space clustering

- Redshift space distrortions
- Fingers of God
- the Kaiser effect
- Projected correlation function $$w_p(r_p) = 2\int_0^\infty d\pi \xi(r_p, \pi) = 2\int_0^\infty dy \xi(r_p^2 + y^2)^{1/2}$$
- 

### 5. Galaxy Bias

-  Galaxies formed in the highest density peaks of the underlying mass distribution will have more clustering than the mass distribution itself.
- Bias is larger at earlier epochs of galaxy formation, as the first galaxy to form will collapse in the most overdense regions of space, which are biased.
- Regardless of initial bias, as time tends to infinity galaxies becomes unbiased tracers of the mass distribution ($b \rightarrow 1$).
- Absolute galaxy bias can also be estimated from the data directly, without having to resort to comparisons with cosmological simulations, by using the ratio of the two-point and three-point correlation functions, which have different dependencies on the bias([Verde et al.(2002)]).

### 8. Halo model interpretation of $\xi(r)$

- NFW profile