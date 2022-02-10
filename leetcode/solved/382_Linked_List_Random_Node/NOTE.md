# Notes on Success
+ By using reservoir sampling we can save space to be O(1),
  but getRandom would take O(N) complexity as we always scan
  the whole list.

+ By turning the linked list into a python array, we can just
  random access the list at random point using random.randrange() 

> Time : O(1) , Space : O(N)
