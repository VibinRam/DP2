From the paper: The Pan-STARRS1 z > 5.6 Quasar Survey. III. The  z $\approx$ 6 Quasar Luminosity Function([2023](https://iopscience.iop.org/article/10.3847/1538-4357/aca7ca))

#### To comprehend from the paper
- How is the quasar survey carried out? What selection function is used?
- How QLF is measured?
- How Ionizing emissivity is calculated?

#### Questions
- Does the QLF at 6 from Schindler et al suggest the need to see more quasars in the search volume of Greiner et al?
- Is there a theoretical model for clustering, halo mass and all that stuff?
- How is it done in simulations?

#### Pointers
- Shindler has papers on Extremely Luminous Quasar Survey for both Pan-STARRS 1 and SDSS
	- The Extremely Luminous Quasar Survey in the Pan-STARRS 1 Footprint (PS-ELQS)([2019](https://iopscience.iop.org/article/10.3847/1538-4365/ab20d0))
	- The Extremely Luminous Quasar Survey in the SDSS Footprint. I. Infrared-based Candidate Selection([2017](https://iopscience.iop.org/article/10.3847/1538-4357/aa9929)) 
- Schindler is making a new research group at Hamburg observatory focusing on quasars in early universe.

#### Abstract and Introduction 

- Type 1 quasars have broad emission lines and Type 2 quasars have narrow emission lines.
- Type 1 quasars are being surveyed here.
- $M_{1450}$ is the x-ray absolute magnitude.
- $h$ in $h^{-1}Mpc$ is :
	- $h = H_0/(100 km s^{-1}Mpc^{-1})$
	- $h$ is included inorder to not introduce the uncertainity in $h$ into distance measurements.
	- $h$ is between $0.66 - 0.73$.
- PS1 sample has $125$ quasars at $z\approx 5.7 - 6.2$, with $-28 \leq M_{1450} \leq -25$.
- Ionizing emissivity $\epsilon_{912}(z = 6) = 7.23 \times 10^22 erg s^{-1}Hz^{-1}cMpc^{-3}$ .
- $\rightarrow$ photoionizing rate of $\Gamma_{HI}(z = 6)\approx6 \times 10^{-16}s^{-1}$ .
- $\rightarrow$ Strongly disfavours dominant role of quasars in hydrogen reionization.

- At low redshift tight correlation is there between the SMBH mass and its host galaxy's properties. This call into attention the role of AGN in galaxy evolution.
- At lower redshifts, the QLF is most effectively describe\hspace{1cm}d by a broken double power law (DPL).
- QLF is described by a break magnitude, a normalization, and two power-law slopes.
- At $z\approx6$, the most comprehensive measurement of the QLF has been presented in [Matsuoka et al. (2018)] using a combined sample from SHELLQs project and previous QLF analyses, with 112 sources. $5.7 < z < 6.5$ and $-30\lesssim M_{1450}\lesssim -22$. 
- Some study show significant decrease in high luminosity quasar density of when we go to higher redshift suggesting quasars has less dominat role in hydrogen reionization.
- Some study like [Giallongo et al (2014, 2019)] and [Grazian et al. (2020)] finds high low luminosity quasar density . But this result is challenged.

- They uses selection strategy of and discoveries from the PS1 distant quasar survey [Banados et al. 2014, 2016, 2022].
- Quasar sample has 125 from PS1 and 48 lower luminosity quasars from SHELLQs [Matsuoka et al. 2018].

#### Quasar candidate selection
- Used PS1 PV2 catalog. It is an internal data release.
- Photometric quality selection: 
	- exclude sources that have been flagged as suspicious by the Imaging Processing Pipeline
	- require 85% of the normalized PSF flux in the _$i_{P1}$_, $z_{P1}$, and $y_{P1}$ bands to be located in unmasked pixels (PSF_QF > 0.85).
- $|b| < 20^o$ excluded for the galactic plane.
- Only sources with modest degrees of galactic reddening is selected, determined from the [Schlegel et al. 1998] dust map. $E(B - V) < 0.3$ is the extinction selection criterion.
- Sources around M31 is excluded. $7^o < R. A. , 14^o$;  $37^o < decl. < 43^o$ . Inclusion results in a large number of candidates which are most likely stars associated with M31.
- Quasar selection get contaminants from M, L, T dwarf stars (or brown dwarfs) also low-redshift galaxies, which appear extended in PS1 seeing conditions. Eliminated using "morphology criterion" ([Banados et al. 2016]).
	- absolute difference between the aperture and PSF magnitudes is below a value of 0.3 in either PS1 z or y band. $|f_{ext,z}| < 0.3$ OR $|f_{ext,y}| < 0.3$.
	- Removes 92% of galaxies while retaining 92% of stars and 97% of quasars.
- At $5.7 \lesssim z \lesssim 6.2$ quasars can be differentiated from brown dwarfs by applying the following selection criteria, [Banados et al. 2014] $$S/N_{z_{P1}} > 10$$ $$S/N_{y_{P1}} > 5$$ $$(z_{P1} - y_{P1}) < 0.5$$ $$((S/N_{i_{P1}} \geqslant 3 \hspace{0.3 cm}\text{AND}\hspace{0.3cm} (i_{P1} - z_{P1}) > 2.0) \hspace{0.3cm} \text{OR} \hspace{0.3cm} (S/N_{i_{P1}} < 3 \hspace{0.3cm} AND \hspace{0.3cm} (i_{P1, lim} - z_{P1} >2.0))$$ $$(S/N_{r_{P1}} < 3 \hspace{0.3cm} \text{OR} \hspace{0.3cm} (r_{P1} - z_{P1}) > 2.2)$$ $$S/N_{g_{P1}} < 3$$applied to stack dereddened PS1 magnitudes.
- Forced photometry is performed on the PS1 stacked and single-epoch images. [Section 2.2 and 2.3 in Banados et al 2014]. Remove all sources where the forced photometry is inconsistent with the reported values in the PS1 PV2 catalog.
- 1032 candidates survived is visualy inspected by Banados and Schindler and a ranking from 1 to 4 is given independently. Final catalogue includes 640 sources with 2, 3 and 4 summed rank.
- Identification efficiency,$$EFF_{ID} = \frac{N_{CQ}}{N_{CQ} + N_{RC}}$$
- Identification completeness, $$S_{ID} = \frac{N_{CQ}}{N_{CQ} + EFF_{ID} \times N_{NoID}}$$
- To avoid biases in completeness of different ranks, they calculate the expected number of quasars for each rank seperately, accounting for the different efficiencies of each sample. $$S_{ID} = \frac{N_{CQ}}{N_{CQ} + \sum_{r=2}^4EFF_{ID,r} \times N_{NoID,r}}$$
- 


#### Results
- 48 quasars from SHELLQs quasar sample presented in [Matsuoka et al. 2018] is included. Their selection function is used.
###### Binned QLF
- Binned QLF over the redshift interval $5.65 \lesssim z \lesssim 6.25$ in bins of absolute magnitude at 1450 $\dot A$. 
- For calculation of binned QLF, **$1/V_a$** method is implemented. [Schmidt 1968; Avni & Bahcall 1980] with the modifications outlined in [Page & Carrera 2000]. See Table 3.

###### ML Estimation of the QLF
- There is only 1 bin in redshift. To get redshift evolution:-
- Assume a parametric model of QLF with redshift evolution.$$\Phi(M, z|\Theta_{QLF})$$is parameterised by $\Theta_{QLF}$.
- Given the observed quasar sample, $N(M,z)$, $$P_{QLF} \equiv P\left(N(M,z)|\Phi(M,z|\Theta_{QLF})\right)$$ can be evaluated.
- Logarithmic probability, $$ln(P_{QLF}) \propto \sum_{j = 1}^{N(M,z)}ln[\Phi(M_j,z_j|\Theta_{QLF})S_j(q(M_j,z_j))] -\Lambda(M,z)$$ is derived from [Marshall et al. 1983]. Where $S(q)$ is the selection function and $\Lambda(M,z)$ is the quasar incidence rate. Derived in the Appendix.
- QLF at low redshift is approximated by a broken DPL [eg. Boyle et al. 2000] $$\Phi(M,z) = \frac{\Phi^*(z)}{10^{0.4(\alpha + 1)(M - M^*)} + 10^{0.4(\beta+ 1)(M - M^*)}}$$ where $\Phi^*$ is normalization, $M^*$ is the break magnitude and $\alpha$ is the faint end slope and $\beta$ is the bright end slope.
- Since the sample has narrow redshift, $$log(\Phi^*(z)) = log(\Phi^*(z = 6)) + k \times (z - 6)$$
- Then we run emcee [Foreman-Mackay et al. 2013] for efficient MCMC sampling of the parameter space.
- Their fiducial model fits the 4 main parameters, while assuming a fixed value for the normalization evolution $k = -0.7$. Motivated by previous QLF measurements at $z \approx 5 - 7$.
- Two main characteristics of the new QLF DPL fit, (see fig. 11)
	- The bright end of the slope is significantly steeper than previous measurements
	- Overall number densities are lower, with the orange curve lying beneath the blue and gray curves for the majority of the magnitude range.
- Variations of the model: (see fig. 12)
	- Varying $k$ shows, best fit for k is $-0.20 \pm 0.2$.
	- Magnitude range of low spectroscopic completeness has a minor influence on our fiducial results.
	- Adding two bright quasar included in [Jiang et al. 2016] and [Matsuoka et al. 2018] is the bright-end test.  Shows individual quasars at the extreme bright end can have significant effect on the QLF measurement.
	- Current redshift range is not large enough to probe the quasar density evolution sufficiently.

#### Discussion
- Fig 13 compares $z = 6$ result from other redshift QLF from literature. Shows rise in quasar number counts from $z = 6.7$ to $3.25$.
- Finds quasar density at the bright end by integrating best fit QLF down to $M_{1450} = -26$.  $n(M_{1450} < -26) = 1.16 cGpc^{-3}$, agrees with other measurements in literature. see Fig. 14.
- Do not find evidence for more rapid decrease of the quasar density at $z > 6.5$.
- Predicts Euclid mission to find 50-70 quasars at $8 \leqslant z < 9$. Drops to 5-8 in the highest redshift bin.
##### Quasar Contribution to Hydrogen Reionization
- $$\Gamma_{HI}(z) = \int_{\nu_{912}}^\infty d\nu \sigma_{HI}(\nu)cn_\nu(\nu,z)$$ where $\sigma_{HI}(\nu)$ is the HI photoionization crosssection and $n_\nu(\nu, z)$ is the number density of the ionizing photons per unit frequency at redshift z.
- 912$\dot A$ is the lyman limit.
- At $z = 6$, we can assume optical depth of the ionizing photons is smaller than unity, allowing for "local source" approximation,$$n_\nu(\nu,z) \approx \frac{(1+z)^3}{h\nu}\frac{l(\nu,z)}{c}\epsilon(\nu,z)$$where $l(\nu,z)$ is the mean free path of the ionizing photons and $\epsilon(\nu,z)$ is the comoving emissivity of the ionizing sources.
- $$l(\nu,z) = l(\nu_{912},z)(\nu/\nu_{912})^{3(\beta - 1)}$$[Faucher-Giguere et al 2008]
- Assumed $\beta = 1.5$ [Madau et al. 1999]
- Assumes powerlaw shape for the extreme UV quasar continuum, with an index of $\alpha_{UV} = 1.7$ [Lusso et al. 2015]$$\epsilon(\nu, z) = \epsilon_{912}(z)\left(\frac{\nu}{\nu_{912}}\right)^{-\alpha_{UV}}$$
- Assuming $\sigma_{HI} \propto \nu^{-3}$, integrate to get,$$\Gamma_{HI}(z) \approx \frac{(1+z)^3}{3 + \alpha_{UV} - 3(\beta - 1)}\epsilon_{912}(z)l(\nu_{912}, z)\sigma_{HI}(\nu_{912})$$
- $\sigma_{HI} = 6.35\times10^{-18}cm^2$ is taken from [Verner et al. 1996].
- Ionizing emissivity is calculated at 1450$\dot A$ :$$\epsilon_{1450}(z) = \int_{-\infty}^{-18}\Phi(M_{1450},z) L_{1450}(M_{1450})dM_{1450}$$
- Now power-law spectral energy distribution distribution for the quasars in the extreme UV $$f_\nu \propto \begin{cases}\nu^{-0.61} & \forall \lambda > 912 \overset{\circ}{A}\\ \nu^{-1.70} & \forall \lambda < 912 \overset{\circ}{A} \end{cases}$$
- Now, $$\epsilon_{912}(z) = \epsilon_{1450} \times (1450 \overset{\circ}A / 912 \overset{\circ}A)^{-0.6}$$
- $$\epsilon_{912}(z = 6) = 7.23^{+1.65}_{-1.02} \times 10^22 ergs^{-1}Hz^{-1}cMpc^{-3}$$
- $l(\nu_{912}, z = 6) = 0.75 pMpc$ at z = 6. [Becker et al. 2021]
- Therefore, $$\Gamma_{HI}(z = 6) = 5.86 \times 10^{-16}s^{-1}$$confusion in error bars.
- 

#### Conclusions
- Fiducial QLF model describes the literature data over $z\approx 4-7$ well without the need for an accelerating decline of the quasar density at $z > 6.5$, as proposed by [Wang et al. (2019b)].
- Estimates an HI quasar photoionization rate 2 orders of magnitude below estimates of its total value.
- 


##### Break magnitude

##### Normalization

##### Two power-law slopes

