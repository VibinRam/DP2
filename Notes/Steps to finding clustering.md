See the one note files 

- End product $$\epsilon(r) = \left(\frac{r}{r_0}\right)^{-\gamma}$$
1. Obtain $r_p$ and $\pi$ of quasars with $z \sim 6$ form PS1. For this we need their redshift and sky positions.
	1. ![[2d redshift space correlation.pdf]]

2. $$\epsilon_s(r_p, \pi)$$Using the Landy & Szalay estimator. $$\xi(s) = \frac{\langle DD\rangle - 2\langle DR \rangle + \langle RR \rangle}{\langle RR\rangle}$$ Need to make a random catalogue here.
	1. ![[2d bin estimator.pdf]]
3. $$\frac{w_p(r_p)}{r_p} = \left(\frac{r_o}{r_p}\right)^\gamma \frac{\Gamma(1/2)\Gamma[(\gamma -1)/2]}{\Gamma(\gamma/2)}$$Is to be fitted with our observation.

- There is [`scipy.spatial`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.count_neighbors.html) that can be used to get the pairs at distance r from a dataset. It uses a better algorithm to find two point correlation function mentioned in this [paper](https://arxiv.org/pdf/astro-ph/0012333.pdf).