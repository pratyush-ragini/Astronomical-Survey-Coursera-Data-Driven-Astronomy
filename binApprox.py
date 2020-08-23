import numpy as np
def median_bins(values, B):
  val_array=np.array(values)
  mu = np.mean(values)
  sigma = np.std(values)
  minval = mu - sigma
  count = 0
  for item in values:
    if item < minval:
      count+=1
  maxval = mu + sigma
  v= val_array[val_array >= minval]
  v2=v[v<maxval]
  #print(v)
  #print(v[v<=maxval])
  #n = len(v[v<=maxval])
  width = (maxval-minval)/B
  #print(width)
  bin_list=[]
  for i in range(0, B):
    vv=val_array[val_array >= (minval+i*width)]
    c=len(vv[vv<minval + width*(1 +i)])
    bin_list.append(c)
  return mu, sigma, count, np.array(bin_list)

def median_approx(values, B):
  length=len(values)
  n = (length +1)/2
  #print(n)
  arr = median_bins(values, B)[3]
  minval = median_bins(values, B)[0] - median_bins(values, B)[1]
  maxval = median_bins(values, B)[0] + median_bins(values, B)[1]
  width = (maxval - minval)/B
  #print(arr)
  summation = median_bins(values, B)[2]
  for i in range(0,B):    
    summation += arr[i]
    if summation >= n:      
      break      
  answer = minval + width*(i + 0.5)
  return answer
