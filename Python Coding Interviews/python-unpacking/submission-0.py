from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    s1, s2, s3 = triplet
    return s1 + s2 + s3


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    l1, l2, l3 = box_dimensions
    return l1*l2*l3
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
