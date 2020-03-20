# kg_imOmesh_2021

Question:
Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
For example, given ​s1 = abc​ and ​s2 = bcd,​ print "​true" into stdout​ since we can map each character in "abc" to a character in "bcd".
Given ​s1 = foo​ and ​s2 = bar,​ print "f​alse"​ since the character ‘o’ cannot map to two characters. But given ​s1 = bar a​ nd ​s2 = foo​, print "true​"​ since each character in "bar" can be mapped to a
character in "foo".

Approach : I used two dictionaries/hashmaps with the count of characters from both the strings respectively. Here, I defined a new function to determine the existence of mapping between these dictionaries. Then, I created a new list from dictionary 1, sorted on the basis of character count.
 I took the minimum character count in string 2, which is greater than the largest occurrence from string 1, which is available in the sorted list based on my intuition that if a character mapping with the minimum occurrence of string 2, which is greater than the largest occurrence in string 1 doesn't exist, the strings can't be mapped even if we choose a higher character count, as we are selecting the extremes. Thereby, I implemented a straight-forward recursion technique, wherein 
 I map these two characters until the largest occurrence from the string 1 has been exhausted, and recursively call the function with the updated dictionaries.
 During this process, if there is no character count equal to or greater than
 the largest occurrence character from string 2, my defined function returns False. If my dictionaries get empty in the process, it indicates that a one-to-one mapping exists between the strings.
