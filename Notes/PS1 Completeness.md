#### Selection function
- $$S(q) = S_\Omega(q) \times S_{morph}(q) \times S_{phot}(q) \times S_{qf}(q) \times S_{ID}(q)$$
- $S_{\Omega}(q)$ is the effective area covered by the survey (footprint).
- $S_{morph}(q)$ is the morphology selection function. Basically the efficiency with which extended sources are rejected. Taken to be $97\%$ in [Banados et al. 2016]
- $S_{phot}(q)$ is the photometric selection function.$$S/N_{z_{P1}} > 10$$ $$S/N_{y_{P1}} > 5$$ $$(z_{P1} - y_{P1}) < 0.5$$ $$((S/N_{i_{P1}} \geqslant 3) \hspace{0.3 cm}\text{AND}\hspace{0.3cm} (i_{P1} - z_{P1}) > 2.0) \hspace{0.3cm} \text{OR} \hspace{0.3cm} (S/N_{i_{P1}} < 3 \hspace{0.3cm} AND \hspace{0.3cm} (i_{P1, lim}) - z_{P1} >2.0))$$ $$(S/N_{r_{P1}} < 3 \hspace{0.3cm} \text{OR} \hspace{0.3cm} (r_{P1} - z_{P1}) > 2.2)$$ $$S/N_{g_{P1}} < 3$$
It is a function of band magnitudes and signal to noice ratios,$$S_{phot}(q) = S_{phot}(r, i , z, S/N_g, S/N_r, S/N_i, S/N_z, S/N_y, i_{lim,dr})$$
- $S_qf(q)$ is the photometric quality selection. 
	- Excluded sources that have been flagged as suspicious by the image processing pipeline.
	- Require 85% of the normalized PSF flux in the $i_{P1}$, $z_{P1}$, and $y_{P1}$ bands to be located in unmasked pixels (PSF_QF > 0.85).

- $S_{ID}(q)$ is the identification completeness.
- Full selection function is given by,
- ![[Pasted image 20230317154513.png|500]]

- Quasar photmetry is simulated using `simqso` inorder to quantify the selection function.