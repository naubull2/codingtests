# Notes on Success
+ Instead of treating the integer as a string then swap,
  mask with 1 to get the right most bit
  then send the result bits to the left (shift left) one bit
  at a time until we have a reversed 32bits. 

> Time : O(1) , Space : O(1)
