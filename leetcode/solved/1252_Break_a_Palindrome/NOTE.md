# Notes on Success
+ if single char is given return "" 
	otherwise
	- replace last non-"a" into "a" while avoiding where this may result in a palindrome
	"aa" all "a",s 
	=> "ab" would be the lex-min

	1. if all a's => replace the last a into b
	2. if not all a's => replace the first non-a into a
	 => except when this char is the exact middle, replace the next non-a character

	O(N) to scan entire list

> Time : O(N) , Space : O(1)
