import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy import units as u
from astropy.coordinates import SkyCoord, Distance
from astropy.cosmology import LambdaCDM as LCDM
from MyToolkit import *
import numpy.ma as ma

DP2_DIRECTORY = "/home/vibin/MyFolder/WorkDesk/DP2/"

cosmo = LCDM(H0=71, Om0=0.26, Ode0=0.74, Ob0=0.0435)

def find_pi_rp(ra_col, dec_col, red_col, rand_ra_col = None, rand_dec_col = None, rand_red_col = None):
    '''Finds r_p and pi from two catalogs given as three arrays of ra (dec deg), dec (dec deg) and redshift. If only 
    1 catalog is given, finds the pairs between that catalog and itself
    '''
    if((rand_ra_col is None) and (rand_dec_col is None) and (rand_red_col is None)):
        rand_ra_col = ra_col
        rand_dec_col = dec_col
        rand_red_col = red_col

    dist_sq1 = np.square(np.array(cosmo.comoving_distance(red_col)))
    dist_sq2 = np.square(np.array(cosmo.comoving_distance(rand_red_col)))
    v1_sq, v2_sq = np.meshgrid(dist_sq1, dist_sq2)

    ps1_quasars1 = SkyCoord(ra_col*u.deg, dec_col*u.deg, cosmo.comoving_distance(red_col))
    ps1_quasars2 = SkyCoord(rand_ra_col*u.deg, rand_dec_col*u.deg, cosmo.comoving_distance(rand_red_col))
    ps1_quasars1.representation_type = 'cartesian'
    ps1_quasars2.representation_type = 'cartesian'
    
    x1 = np.array(ps1_quasars1.x)
    y1 = np.array(ps1_quasars1.y)
    z1 = np.array(ps1_quasars1.z)
    x2 = np.array(ps1_quasars2.x)
    y2 = np.array(ps1_quasars2.y)
    z2 = np.array(ps1_quasars2.z)    
    x1, x2 = np.meshgrid(x1, x2)
    y1, y2 = np.meshgrid(y1, y2)
    z1, z2 = np.meshgrid(z1, z2)

    v1_v2 = x1*x2 + y1*y2 + z1*z2

    pi_array = np.absolute((v2_sq - v1_sq)/np.sqrt(v1_sq + v2_sq + 2 * v1_v2))
    rp_array = np.sqrt(np.absolute(v1_sq + v2_sq - 2 * v1_v2 - np.square(pi_array)))

    pi_array = pi_array[np.triu_indices(len(pi_array),k = 1)]
    rp_array = rp_array[np.triu_indices(len(rp_array),k = 1)]

    return pi_array, rp_array
    #return v1_sq, v2_sq, v1_v2

def find_s_bined(ra_col, dec_col, red_col, rand_ra_col = None, rand_dec_col = None, rand_red_col = None):

    if((rand_ra_col is None) and (rand_dec_col is None) and (rand_red_col is None)):
        rand_ra_col = ra_col
        rand_dec_col = dec_col
        rand_red_col = red_col

    ps1_quasars1 = SkyCoord(ra_col*u.deg, dec_col*u.deg, cosmo.comoving_distance(red_col))
    ps1_quasars2 = SkyCoord(rand_ra_col*u.deg, rand_dec_col*u.deg, cosmo.comoving_distance(rand_red_col))
    ps1_quasars1.representation_type = 'cartesian'
    ps1_quasars2.representation_type = 'cartesian'
    
    x1 = np.array(ps1_quasars1.x)
    y1 = np.array(ps1_quasars1.y)
    z1 = np.array(ps1_quasars1.z)
    x2 = np.array(ps1_quasars2.x)
    y2 = np.array(ps1_quasars2.y)
    z2 = np.array(ps1_quasars2.z)
    x1, x2 = np.meshgrid(x1, x2)
    y1, y2 = np.meshgrid(y1, y2)
    z1, z2 = np.meshgrid(z1, z2)

    s_array = np.sqrt(np.power(x2 - x1, 2) + np.power(y2 - y1, 2) + np.power(z2 - z1, 2))
    s_array = s_array[np.triu_indices(len(s_array),k = 1)]

    return s_array
    

def make_rand_cat(num):
    ind = np.where(np.arange(num) > -1)
    rand_ra = np.zeros(num)
    rand_dec = np.zeros(num)
    while True:
        ### using Archimede's theorem
        rand_ra[ind] = np.random.uniform(0, 360, len(ind[0]))
        rand_dec[ind] = np.degrees(np.arcsin(np.random.uniform(-0.5, 1, len(ind[0]))))
        ind = np.where(np.absolute(np.arcsin(np.cos(np.radians(rand_dec)) * np.cos(np.radians(27.4)) * np.cos(np.radians(rand_ra - 192.25)) \
                                            + np.sin(np.radians(rand_dec)) * np.sin(np.radians(27.4)))) < np.radians(20))
        if(len(ind[0]) == 0):
            break

    rand_red = np.random.uniform(5.7, 6.2, num)

    return rand_ra, rand_dec, rand_red

def find_wp_rp_single_bin(ra, dec, red, file_name):
    rand_ra, rand_dec, rand_red = make_rand_cat(len(ra))

    pi_array, rp_array = find_pi_rp(ra, dec, red)
    rand_pi_array, rand_rp_array = find_pi_rp(rand_ra, rand_dec, rand_red)
    cross_pi_array, cross_rp_array = find_pi_rp(ra, dec, red, rand_ra_col=rand_ra,\
                                                rand_dec_col=rand_dec, rand_red_col=rand_red)

    rp_bins = np.float_power(10, np.arange(31) * 0.15)
    rp_mid = (rp_bins[:-1] + rp_bins[1:])/2

    rp_hist = (plt.hist(rp_array, rp_bins)[0]).astype(int)
    rand_rp_hist = (plt.hist(rand_rp_array, rp_bins)[0]).astype(int)
    cross_rp_hist = (plt.hist(cross_rp_array, rp_bins)[0]).astype(int)
    plt.close()

    unfin_pos = np.where(rp_hist * rand_rp_hist * cross_rp_hist == 0)

    with np.errstate(divide='ignore', invalid='ignore'):
        xi_rp = (rp_hist - 2 * cross_rp_hist + rand_rp_hist)/rand_rp_hist
    xi_rp_masked = ma.array(xi_rp)
    xi_rp_masked[unfin_pos] = ma.masked

    file = open(DP2_DIRECTORY + "Data/" + file_name + ".txt", 'w')
    file.write('   rp_mid       DD      RR      DR      xi_rp \n')
    for i in range(len(rp_mid)):
        file.write(f'{rp_mid[i]:9.3f}   {rp_hist[i]:5d}    {rand_rp_hist[i]:5d}   {cross_rp_hist[i]:5d}   {xi_rp[i]:8.5f}\n')

    #xi_rp = np.abs(xi_rp)
    #(rp_hist + rand_rp_hist - 2 * cross_rp_hist)/rand_rp_hist
    fig, ax = plt.subplots()
    ax.plot(rp_mid, xi_rp_masked/rp_mid, '*--')
    ax.set_ylabel(r'$w_p(r_p)/r_p$')
    ax.set_xlabel(r'$r_p (Mpc)$')
    ax.axhline(0, ls = '--', lw = 0.5, c = 'black')

    return ax

def find_xi_s(ra, dec, red, file_name):
    rand_ra, rand_dec, rand_red = make_rand_cat(len(ra))

    s_array = find_s_bined(ra, dec, red)
    rand_s_array = find_s_bined(rand_ra, rand_dec, rand_red)
    cross_s_array = find_s_bined(ra, dec ,red, rand_ra_col=rand_ra, rand_dec_col=rand_dec, rand_red_col=rand_red)

    s_bins = np.float_power(10, np.arange(43)*0.1)
    s_mid = (s_bins[:-1] + s_bins[1:])/2

    s_hist = (plt.hist(s_array, s_bins)[0]).astype(int)
    rand_s_hist = (plt.hist(rand_s_array, s_bins)[0]).astype(int)
    cross_s_hist = (plt.hist(cross_s_array, s_bins)[0]).astype(int)
    plt.close()

    unfin_pos = np.where(s_hist * rand_s_hist * cross_s_hist == 0)

    with np.errstate(divide='ignore', invalid='ignore'):
        xi_s = (s_hist - 2 * cross_s_hist + rand_s_hist)/rand_s_hist
    xi_s_masked = ma.array(xi_s)
    xi_s_masked[unfin_pos] = ma.masked

    file = open(DP2_DIRECTORY + "Data/" + file_name + ".txt", 'w')
    file.write('   s_mid       DD      RR      DR      xi_s \n')
    for i in range(len(s_mid)):
        file.write(f'{s_mid[i]:9.3f}   {s_hist[i]:5d}    {rand_s_hist[i]:5d}   {cross_s_hist[i]:5d}   {xi_s[i]:8.5f}\n')

    fig, ax = plt.subplots()
    ax.plot(s_mid, xi_s_masked, '*--')
    ax.set_ylabel(r'$xi(s)$')
    ax.set_xlabel(r'$s (Mpc)$')
    ax.axhline(0, ls = '--', lw = 0.5, c = 'black')

    return ax