WeFrom Shen et. al. 2007.

- Sample contains 4,426 luminous optical quasars
- Redshift $2.9 \leq z \leq 5.4$
- Power law fit $\xi(r) = (r/r_0)^{-\gamma}$: 
	- $r_0 = 15.2 \pm 2.7 h^{-1}Mpc$.
	- $\gamma = 2.0 \pm 0.3$
	- Scale range $4 \leq r_p \leq 150 h^{-1}Mpc$
- For $z \approx 1.5$, $r_0 \approx 6.5 h^{-1}Mpc$
- Sample is devided into two redshift bins assuming $\gamma = 2.0$:-
- $2.9 \leq z \leq 3.5$:
	- $r_0 = 16.9\pm 1.7h^{-1}Mpc$
	- $Duty = 0.004 \sim 0.05$ 
	- $t_Q = 4 \sim 50 Myr$
	- $M_{min} = 2-3 \times 10^{12} h^{-1}M_0$
	- $b_{eff}\sim8$ at $z=3.0$
- $z \geq 3.5$:
	- $r_0 = 24.3\pm 2.4 h^{-1}Mpc$
	- $Duty = 0.03 \sim 0.6$
	- $t_Q = 30 \sim 600 Myr$
	- $M_{min} = 4-6\times10^{12}h^{-1}M_0$
	- $b_{eff} \sim 16$ at $z = 4.5$


### Questions

- Why data is devided into two bins?
- What does it mean to say, quasar locus crosses the stellar locus in color space at $z \approx 2.7$ [Fan 1999]?
- What is the quasar selection algorithm in SDSS?
- Overlapping plates?
- Projected correlation function is what we are getting from direct astrometry observation? - Girish agrees.
- What is scale range?
- How they decide $\pi_{cutoff}$ for integration over line of sights of $\xi(r_p, \pi)$?
- 
### Sample selection $f(z)$

- 2.5 wide-field telescope, drift scan camera with 30 CCDs, images sky in 5 boad bands ($ugriz$)
- Candiates for followup spectroscopy are selected using their colors, and arranged in spectro plates for [[double spectroscopy]]
- Spectroscopy is carried out over 5740 $deg^2$.
- Selection algorithm:
	- $z\leq 3.5$ are outliers from the stellar locus in the ugri color cube.
	- $z>3.5$ are outliers from the griz color cube.
- Quasar candidate sample is flux limited to $i = 19.1$ and at $z > 3$ to $i = 20.2$.

### Redshift space correlation function

- Redshift space is where distances are obtained from redshift without any corrections for peculiar velocity of redshift errors.
- Redshift space correlation function[Landy & Szalay(1993)](https://ui.adsabs.harvard.edu/abs/1993ApJ...412...64L/abstract)$$\xi(s) = \frac{\langle DD\rangle - 2\langle DR \rangle + \langle RR \rangle}{\langle RR\rangle}$$
- **Jackknife d10**:  10 spatially contiguous subsambles are made from the data sets and jackknife samples are created by omitting each of these samples in turn and mean of the number of data points in bin $s$ for each jackknife samble is taken as $DD_{mean}$, used in place of $\langle DD \rangle$. Covaraince matrix is calculated as,$$Cov(\xi_i,\xi_j) = \frac{N-1}{N}\sum^N_{l=1} (\xi_i^l - \bar\xi_i)(\xi_j^l - \bar\xi_j)$$
- **Poisson error estimator**: 

### Real Space correlation function

- Redshift space distortion due to peculiar motion of quasars in the cluster, called **Fingers of God**.![Alt test](https://ned.ipac.caltech.edu/level5/March12/Coil/Figures/figure4.jpg "Fingers of God")
- Projected correlation function $w_p(r_p)$: $$w_p(r_p) = 2 \int_0^\infty d\pi \xi_s(r_p, \pi)$$ $2$?
- where, $$\pi = \frac{s\cdot l}{|l|} \hspace{1cm} r_p = \sqrt{s\cdot s - \pi^2}$$[Fisher et al 1994] originally from coil notes.
- In practice integration is only upto $\pi_{cutoff} = 100h^{-1}Mpc$. 
- Now relation between projected correlation function and real space correlation function:$$w_p(r_p) = 2\int_0^\infty dy\xi(\sqrt{r_p^2 + y^2})$$$$w_p(r_p) = 2\int_0^\infty \frac{rdr}{\sqrt{r^2 - r_p^2}}\xi(r)$$Assuming power law $\xi(r) = \left(\frac{r}{r_0}\right)^{-\gamma}$$$w_p(r_p) = r_p\left(\frac{r_o}{r_p}\right)^\gamma \frac{\Gamma(1/2)\Gamma[(\gamma -1)/2]}{\Gamma(\gamma/2)}$$
- Now angular correlation function can be fitted with this function to obtain $\gamma$ and $r_0$.
- The predicted correlation of the underlying dark matter at $r = 15h^{-1}Mpc$ is $\sim 0.014$ at $z = 3.5$, far below that of the current high redshift quasar sample $\sim 22.92$. [Fig. 5, Shen et al. (2006)]
- The clustering of quasars increases strongly with redshift over the range probed by the sample.[Table 4, Shen et al. (2006)]

### Quasar lifetime, Threshold Halo mass, Effective bias

- Quasar spatial density, $$\Phi(z) = \int_{M_{min}}^\infty dM \frac{t_Q}{t_H(M,z)}n(M,z)$$Adopted values of $\phi(z)$ are taken from the Maximum Likelihodd fitted quasar luminosity function with variable power law index given by [Richard et al. (2006)], integrated from the faintest $i$-band magnitude $i = 20.2$, with some corrections. QLF is the quasar number density as a function of luminosity and redshift.
- Assumptions are:
	0. Every dark matter halo harbors a SMBH, either active or dormant, and the resulting quasars have same clustering strength as their hosting halos.
	1. Luminous quasars only reside in dark matter halos with mass above some threshold $M_{min}$.
	2. Dark matter halos with $M \geq M_{min}$ host at most one active quasar at a time.
	3. Probability that halo harbors an active quasar is the duty cycle $\frac{t_Q}{t_H}$
	4. 
-  Halo mass function,$$n(M,z)dM = -A\sqrt{\frac{2a}{\pi}}\frac{\rho_0}{M}\frac{\delta_c(z)}{\sigma^2(M)}\frac{d\sigma(M)}{dM}\left\{1 + \left[\frac{\sigma^2(M)}{a\delta^2_c(z)}\right]^p\right\}\exp{\left[-\frac{a\delta^2_c(z)}{2\sigma^2(M)}\right]}dM$$[Sheth & Tormen(1999)]
- $t_H(M,z)=t_U(z_2) - t_U(z)$. [Lacey & Cole (1993)].
- Assuming a $t_Q$, we can compute $M_{min}$ from equation of $\Phi(z)$.
- $M_{min}$ gives $b_{eff}(M_{min},z)$. $$b_{eff}(M_{min},z) = \int_{M{min}}^\infty dM\frac{b(M,z)n(M,z)}{t_H(M,z)}\left[\int_{M_{min}}^\infty dM\frac{n(M,z)}{t_H(M,z)}\right]^{-1}$$
- $b(M,z)$ from [Jing (1998)]
- $$\xi_{model}(r,z) = b_{eff}^2\xi_m(r,z) = b_{eff}^2\xi_{m}(r)D^2(z)$$$\xi_{m}(r)$ is the present-day mass correlatioin function. $$\xi_m(r) = \frac{1}{2\pi^2}\int_0^\infty dk k^2P(k)\frac{\sin kr}{kr}$$$D(z)$ is the linear growth factor of fluctuations.
- Averaging over certain redshift range,$$\bar\xi(r) = \frac{\int dV_c n^2_{QSO}(z)\xi_{model}(r,z)}{\int dV_c n^2_{QSO}(z)}$$
- Iterate to find $t_Q$ which minimizes the difference between $\bar\xi(r)$ and $\xi(r)$. In practice use $\xi_{20}$.[Table 5, Shen et al. (2006)] $$\xi_{20} = \frac{3}{r^3_{max}}\int_{r_{min}}^{r_{max}}\xi(r)r^2dr$$$$\xi_{20} = \frac{3r_0^\gamma}{(3-\gamma)r^3_{max}}(r_{max}^{3-\gamma}-r_{min}^{3-\gamma})$$$r_{min} = 5h^{-1}Mpc$ and $r_{max} = 20h^{-1}Mpc$.

### Appendix A. Quasar redshift determination

- Mg II line has a small and known offset from the systemic redshift. 


## Intro to the paper

- The galaxy 2P correlation function is well fit with a power law:$$\xi(r) = \left(\frac{r}{r_0}\right)^{-\gamma}$$ on scales $r \leq 20 h^{-1}Mpc$, with comoving correlation length $r_0\sim5h^{-1}Mpc$ and slope $\gamma \sim 1.8$. 
- Quasars are interpreted as a strochastic process through which every luminous galaxy passes, and therefore the clustering of quasars should be no different from that of luminous galaxies.
- Paper presents the correlation function of high redshift$(z \geq 2.9)$ quasars using the fifth data release of the SDSS, containing 6,000 quasars.
- Redshift space correlation function[Landy & Szalay(1993)]$$\xi(s) = \frac{\langle DD\rangle - 2\langle DR \rangle + \langle RR \rangle}{\langle RR\rangle}$$
- Myunderstanding: A histogram of redshift seperation between each of the data points in Data catalogue, Random catalogue and cross seperation between data and random catalogue is made. $\langle DD\rangle$ is the normalised number of data points in the bin with redshift $s$. 
- Bootstrap, Jackknife and Poisson estimator can be used to estimate the error. Jackknife and Poisson is used in this paper.
- **Jackknife**:  10 spatially contiguous subsambles are made from the data sets and jackknife samples are created by omitting each of these samples in turn and mean of the number of data points in bin $s$ for each jackknife samble is taken as $DD_{mean}$, used in place of $\langle DD \rangle$. Covaraince matrix is calculated as,$$Cov(\xi_i,\xi_j) = \frac{N-1}{N}\sum^N_{l=1} (\xi_i^l - \bar\xi_i)(\xi_j^l - \bar\xi_j)$$
- Quasar spacial density,$$\Phi(z) = \int_{M_min}^\infty dM\frac{t_Q}{t_H(M, z)}n(M,z)$$
- 