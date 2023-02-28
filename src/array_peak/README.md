# Description:
Give an integer array of length at least 2, find any peak of the array. An index i is a pick of array if the element at i is larger of equal than it’s neighbouring element(s). For any index i, i-1 and i+1 are the neighbours. First and last element only has one neighbour.
For this problem, we want to do multiple swap operations and find peak after each operation.
### Input:
Array:
[1, 3, 4, 5, 2, 1, 1]
### Swap Operations:
0 1
3 4
### Expected Output:
3 (index of the peak, not the element itself)
4 (index of the peak, not the element itself)
If there are multiple solutions, output any of them is good.
## Constraints:
* Array size will be between 2 and 1 million
* There can be millions of queries. Each query will have this format i j where i and j both >= 0 and < array size. Also i < j.

## Instructions
Cannot iterate the whole array.