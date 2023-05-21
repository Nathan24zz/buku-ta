import numpy as np
import math

def cosine_distance(self, A, B):
    # reduce dimension ([[x, y]] -> [x, y])
    A = A.reshape(2,)
    B = B.reshape(2,)

    nominator = np.dot(A, B)
    denominator = np.linalg.norm(
        A) * np.linalg.norm(B)
    if denominator == 0: 
        cosine_similarity = 0
    else: 
        cosine_similarity = nominator / denominator
    return_val = math.sqrt(2 * (1 - cosine_similarity))
    
    return return_val
