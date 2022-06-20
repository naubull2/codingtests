# Notes on Success
+ We can easily come up with a max-heap solution
  where O(logk) heap maintainance is used for keeping
  "top-k" (closest) elements in a single scan through points.
	Resulting in O(nlogk) time / O(k) space

+ To go further, we can binarysearch radius(distance) R,
  until we have K elements within the radius R.
  since removing confirmed points, (approximately halves)
  N + N/2 + N/4 + .... N/N = 2N
  so O(N) time complexity

> Time : O(N) , Space : O(N)
