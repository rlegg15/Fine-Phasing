# Fine-Phasing
This is a store of Python programs used to test fine phasing algorithms for L2 SC linac
I used a linear fit for the zero crossing calculation and a cosine fit for the full -180 to +180 degrees measurements.
The value of each point was calculated exactly and then a random amount correspoinding to plus/minus 0.5x the BPM resolution was added.
The array of the degrees offset vs values was fit using the numpy linear regression for the zero crossing runs and the optimize.curve_fit function 
from scipy for the cos fits.  In each case the calculated intercept (Crest for cavity) was calculated.  
To qualitatively judge the two techniques, 10000 runs were made at zero degrees in each case and the std dev (from statistics module) of the solutions 
were tabulated. The Probability Distribution Function (from stat.norm) of the results was plotted to show graphically the variation.
