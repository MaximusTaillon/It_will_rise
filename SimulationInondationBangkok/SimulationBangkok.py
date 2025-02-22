import matplotlib.pyplot as plt
import matplotlib.image as img 
from scipy.ndimage import gaussian_filter 
import numpy as np 
import matplotlib.patches as patches

def augmentationDeLEAU(t):
    valeur = 0.0572*t*t + 19.37*t
    return(valeur)
    

topographie = np.array([
[ 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 23, 7, 7, 7, 7, 7],
[ 7, 7, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7],
[ 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7,
7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7],
[ 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 23, 23, 29, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 23, 23, 23, 23, 23, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7],
[ 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 23, 23, 23, 23, 7, 7, 7, 7, 7, 29, 29, 29, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 23, 23, 23, 23, 23, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 23, 23, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 23, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 23, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 16, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 16, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 23, 23, 23, 7, 23],
[ 7, 7, 7, 7, 7, 7, 16, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 23],
[ 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 16, 7, 23, 23, 7, 7, 7, 7, 23, 23, 16, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 23, 7, 23, 7, 7, 7, 7, 7, 7, 7, 29, 7, 7, 7, 23],
[ 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 23, 23, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 7, 7, 16, 7, 23, 7, 7, 7, 7, 7, 7, 23],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 23, 23, 7, 23, 23, 29],
[ 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 7, 23, 7, 23, 23, 23],
[ 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 23, 23, 7, 23, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 23, 7, 7, 7, 7, 23, 23, 23],
[23, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 7, 7, 23, 23, 23, 23, 23, 7, 23, 23, 23, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 23, 23, 23],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 7, 23, 23, 23, 23, 23, 23, 23, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 7, 23, 7, 23, 23, 7, 23, 23, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 23, 7, 7, 7, 23, 23, 23, 7, 7, 7, 23, 23, 23, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 23, 29, 23, 7, 7,
7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 23, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 7, 23,
7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 29, 23, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 23, 23, 23, 23, 7, 23, 29, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 7, 7, 7, 23, 23, 7, 7, 7, 23, 23, 23, 23, 23, 7,
7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 23, 23, 23, 7, 23, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 7, 7, 7, 23, 23, 23, 23, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7, 23, 23, 7, 23, 7, 7,
7, 7, 7, 7, 7, 2, 7, 23, 29, 23, 7, 7, 7, 23, 23, 7, 7, 7, 7],
[ 7, 7, 7, 7, 23, 23, 7, 7, 23, 23, 7, 7, 7, 23, 7, 7, 23, 23, 7, 7, 7, 23, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7,
7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 23, 23, 23, 23, 23, 23],
[ 7, 7, 7, 23, 23, 23, 7, 7, 7, 7, 7, 23, 23, 7, 23, 23, 23, 23, 23, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 29, 23],
[ 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 23, 23, 23, 23, 23, 23, 7, 7, 7, 7, 7, 23, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7,
7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 23, 23],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7],
[ 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 23, 23, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7],
[ 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 23, 23, 16, 23, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 16, 23, 7, 7, 7, 23, 23, 7, 7, 7, 7],
[ 2, 2, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 23, 7, 23, 7, 7, 23, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 23, 7, 7, 16, 7, 7, 23, 23, 23, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 23, 7, 23, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 23, 23, 7, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 2, 7, 7, 7, 7, 23, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 7, 23, 23, 23, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 23, 23, 23, 29, 23, 23, 23, 23, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7,
7, 7, 7, 7, 7, 7, 7, 16, 23, 23, 23, 23, 23, 23, 7, 7, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 7,
7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 23, 23, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 23, 23, 23, 29, 23],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 23, 23, 7, 7, 7, 23, 7, 7, 7, 23, 23, 7, 7,
7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 23, 7, 7, 23, 23, 7, 7, 23, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 7, 7, 7, 7, 7, 7, 2, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23,
23, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 23, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 2, 2, 2, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 23, 7, 7, 7, 7, 23, 7, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 23, 23, 23, 23, 7, 7, 7, 7, 7, 7, 7, 23,
23, 7, 7, 23, 23, 23, 7, 23, 23, 23, 7, 23, 23, 23, 7, 23, 23, 7, 7],
[ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 2, 2, 23, 23, 7, 23, 7, 7, 7, 7, 7, 7, 7, 23, 7,
23, 23, 7, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 7, 7, 7]
])

topographie = topographie.astype(float)

topographie = gaussian_filter(topographie, sigma=1)

    
im = img.imread('bangkok.png') 

for t in range(276):
    fig,plan = plt.subplots(1)

    plan.imshow(im)
    
    niveauDeLeau = augmentationDeLEAU(t)/1000
    print(t)
    
    for i in range(55):
        for j in range(55):
            valeurCoordonnee = topographie.item((i,j))
            
            if(valeurCoordonnee < niveauDeLeau):
                 
                rect = patches.Rectangle((10*i, 10*j),10, 10)
                plan.add_patch(rect)
                
    plt.axis('off')         
    plt.title(str(2025+t))
    plt.savefig("EtatBangkok" + str(t+2025) + ".png", format="png")


