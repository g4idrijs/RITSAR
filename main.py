##############################################################################
#                                                                            #
#  This is the main file that calls in inputs from the parameter files and   #
#  passes them to an image processing algorithm of choice.  Parameters are   #
#  defined in the './parameters/*.py' files.  Adjust the parameters in these #
#  these files to match your collection configuration.                       #
#                                                                            #
##############################################################################

#Add include directories to default path list
from sys import path
path.append('./parameters')
path.append('./include')

#Include dependencies
import numpy as np
import matplotlib.pylab as plt
#from read_auxillary import aux_read
from SARplatformUHF import plat_dict
from img_plane import img_plane_dict
from simulate_phs import sim_phs
from phs_to_const_ref import phs_const_ref
from RVP_correct import RVP_corr
from backprojection import bp
from polar_format import pf
from omega_k import wk

#Import auxillary data
#fname = './*.aux'
#aux = aux_read(fname)

#Import platform dictionary from './parameters/SARplatform'
platform = plat_dict()

#Import image plane dictionary from './parameters/img_plane'
img_plane = img_plane_dict(platform)

#Simulate phase history, if needed
##############################################################################
nsamples = platform['nsamples']
npulses = platform['npulses']
x = img_plane['u']; y = img_plane['v']
points = [[0,0,0],
          [0,-100,0],
          [200,0,0]]
amplitudes = [1,1,1]
sim_phs(platform,
        points = points, amplitudes = amplitudes, window = 1)
##############################################################################

#Import phase history data
phs = np.load('./phase_history.npy')

#Apply RVP correction
[phs_corr, platform] = RVP_corr(phs, platform)

#Demodulate phase history with constant reference, if needed 
[phs_fixed, platform] = phs_const_ref(phs_corr, platform, upchirp = 1)

#Apply algorithm of choice to phase history data
img_wk = wk(phs_fixed, platform, img_plane, taylor = 43, upsample = 2)
#img_bp = bp(phs_corr, platform, img_plane, taylor = 0, upsample = 2)
#[img_pf, phs_polar] = pf(phs_corr, platform, img_plane, taylor = 43)

#Output image
plt.imshow(np.abs(img_wk))