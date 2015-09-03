import os
import sys
import pandas as pd
import glob

def binary_search(L, v):
    lengthOfL = len(L)
    imin = 0
    imax = lengthOfL # imax always points to end of array (non inclusive).
    while imin < imax:
        # Computes midpoint for roughly equal partition.
        imid = int((imin + imax) / 2)
        if v == L[imid]:     # v found at index imid.
            return L[imid]
            break
        elif v < L[imid]:    # Changes imax index to search lower subarray.
            imax = imid
        else:                            # Changes imin index to search upper subarray.
            imin = imid + 1
 
    if imin < imax:            # Found v
        # Handles repetitions: makes imid point to 1st greater than v.
        while imid < lengthOfL and v == L[imid]:
            imid += 1
        # return L[imid]
        return True
    else:
        # return -1
        return False