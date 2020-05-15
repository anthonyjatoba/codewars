def twos_difference(lst): 
  slst = sorted(lst)
  pairs = []
  for i in range(len(slst)):
      for j in range(1, len(slst)):
          if slst[j] - slst[i] == 2:
              pairs.append((slst[i], slst[j]))
  return pairs