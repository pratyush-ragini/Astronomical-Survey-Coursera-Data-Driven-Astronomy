from helper import running_stats
import numpy as np
from astropy.io import fits
# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(file_list, N):
  mean, std = running_stats(file_list)
  dim = mean.shape
  ignore_bin = np.zeros(dim)
  bin_array = np.zeros((dim[0], dim[1], N))
  #print(bin_array)
  width = 2*std/N
  #print(dim)
  #print(dim[0], dim[1], N)
  for item in file_list:
    hdulist = fits.open(item)
    data= hdulist[0].data
    for i in range(dim[0]):
      for j in range(dim[1]):
        value = data[i,j]
        mu = mean[i,j]
        sigma = std[i,j]
        if value<(mu-sigma):
          ignore_bin[i,j] +=1
        
        elif value>=(mu-sigma) and value<(mu+sigma):
          bin_number = int((value - (mu-sigma))/width[i,j])
          bin_array[i, j, bin_number]+=1
  return mean, std, ignore_bin, bin_array
  
def median_approx_fits(file_list, N):
  mean, std, ignore_bin, bin_array = median_bins_fits(file_list, N)
  width=2*std/N
  dim = mean.shape
  M = len(file_list)
  middle=(M+1)/2
  median=np.zeros(dim)
  
  for i in range(dim[0]):
    for j in range(dim[1]):
      count = ignore_bin[i,j]
      for a, b in enumerate(bin_array[i,j]):
        count+=b
        if count>=middle:
          break
      median[i,j] = mean[i,j] - std[i,j] + width[i,j]*(a+0.5)
  return median
                                                       
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['images/image0.fits', 'images/image1.fits', 'images/image2.fits'], 5)
  median = median_approx_fits(['images/image0.fits', 'images/image1.fits', 'images/image2.fits'], 5) 
  data  = median_approx_fits(['images/image0.fits', 'images/image1.fits', 'images/image2.fits', 'images/image3.fits'], 5)
 
  # Plot of the result
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
