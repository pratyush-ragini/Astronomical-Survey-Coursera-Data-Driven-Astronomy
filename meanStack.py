def mean_fits(file_list):
  import numpy as np
  from astropy.io import fits
  n=len(file_list)
  if n>0 :
    hdulist=fits.open(file_list[0])
    data=hdulist[0].data
    for i in range(1,n):
      hdulist=fits.open(file_list[i])
      data+=hdulist[0].data
    m=data/n
    return m

if __name__ == '__main__':  
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits'])
  print(data[100, 100])
  # Plot of the result
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
