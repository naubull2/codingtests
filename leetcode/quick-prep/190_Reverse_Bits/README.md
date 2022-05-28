### [190. Reverse Bits](https://leetcode.com/problems/reverse-bits)

Easy

Reverse bits of a given 32 bits unsigned integer.

__Note:__

*   Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
*   In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2's complement notation</a>. Therefore, in __Example 2__ above, the input represents the signed integer `` -3 `` and the output represents the signed integer `` -1073741825 ``.

 

__Example 1:__

```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

__Example 2:__

```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

 

__Constraints:__

*   The input must be a __binary string__ of length `` 32 ``

 

__Follow up:__ If this function is called many times, how would you optimize it?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 967,757 | 477,622 | 49.4% |