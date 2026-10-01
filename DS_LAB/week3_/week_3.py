import numpy as np
from scipy.spatial import distance

pA = np.array([7, 4, 6,9]);
pB = np.array([5, 1, 5,4])

e_dist = distance.euclidean(pA, pB)
print("Euclidean distance: ", e_dist)

similarity_e = 1/(1+e_dist)
print("Euclidean Similarity: ", similarity_e)

m_distance = distance.cityblock(pA, pB)
print("Manhattan Distance:", m_distance)

similarity_m = 1/(1+m_distance)
print("Manhattan Similarity", similarity_m)

min_dist_p2 = distance.minkowski(pA,pB,p=2)
print("Minkowski Distance (p=2):", min_dist_p2)

similarity_min = 1/(1+(min_dist_p2))
print("Minkowski Similarity (p=2):",similarity_min)

min_dist_p1 = distance.minkowski(pA,pB,p=1)
print("Minkowski Distance (p=1):", min_dist_p1)

similarity_min = 1/(1+(min_dist_p1))
print("Minkowski Similarity (p=1):",similarity_min)

min_dist_p3 = distance.minkowski(pA,pB,p=3)
print("Minkowski Distance (p=3):", min_dist_p3)

similarity_min = 1/(1+(min_dist_p3))
print("Minkowski Similarity (p=3):",similarity_min)