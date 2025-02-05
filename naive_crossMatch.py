import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, radius):
  start = time.perf_counter()
  radius = np.radians(radius)
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  dec_order = np.argsort(cat2[:,1])
  #print(dec_order)
  cat2_order = cat2[dec_order]
  order_dec = cat2_order[:,1]
  #print(order_dec)
    
  matches = []
  no_matches = [] 
  for id1, (ra1, dec1) in enumerate(cat1):
    max_1 = dec1 + radius
    min_1 = dec1 - radius
    min_index = np.searchsorted(order_dec, min_1, side= 'left')
    max_index = np.searchsorted(order_dec, max_1, side= 'right')
    min_dist = np.inf
    min_id = None
    for id2, (ra2, dec2) in enumerate(cat2_order[min_index:max_index], min_index):      
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id = dec_order[id2]
        min_dist = dist       
    if min_dist > radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id, np.degrees(min_dist)))    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
