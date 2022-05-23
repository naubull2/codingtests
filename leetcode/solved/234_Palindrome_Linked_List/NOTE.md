# Notes on Success
+ Use fast/slow two pointer scan,
  along the way, reverse the slow chain
  - we now have two pointers going from center to left/right end
  - this may break the original chain so might as well restore before returning
    (for actual application)

> Time : O(N) , Space : O(1)
