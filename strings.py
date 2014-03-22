#! python
# working with strings

# We can concatenate atrings with the + operator, and repeat with *: 

phrase = 'Internet' + 'of' + 'Things '
print phrase

print '<' + phrase*5 + '>'

# Two string literals next to each other are automatically concatenated; 
# the first line above could also have been written "phrase = 'Help' 'A'"; 
# this only works with two literals, not with arbitrary string expressions: 

st='str' 'ing'             #  <-  This is ok
print st
st='str'.strip() + 'ing'   #  <-  This is ok
print st

# Strings can be indexed; like in C, the first character of a string 
# has index 0. There is no separate character type; a character is 
# simply a string of size one. Like in Icon, substrings can be specified with 
# the slice notation: two indices separated by a colon. 

print phrase[4]

print phrase[0:2]

print phrase[2:4]

# Slice indices have useful defaults; an omitted first index defaults to zero, 
# an omitted second index defaults to the size of the string being sliced. 

print phrase[:2]    # The first two characters
print phrase[2:]    # All but the first two characters

# Python strings cannot be changed. Assigning to an indexed position in the string results in an error: 
# However, creating a new string with the combined content is easy and efficient: 

print 'w' + phrase[1:]

print 'Know' + phrase[4]

# Here's a useful invariant of slice operations: s[:i] + s[i:] equals s. 

print phrase[:2] + phrase[2:]

print phrase[:3] + phrase[3:]


# Degenerate slice indices are handled gracefully: an index that is too large is replaced 
# by the string size, an upper bound smaller than the lower bound returns an empty string. 

print phrase[1:100]

print phrase[10:]

print phrase[2:1]


# Indices may be negative numbers, to start counting from the right. For example: 


print phrase[-1]     # The last character

print phrase[-2]     # The last-but-one character

print phrase[-2:]    # The last two characters

print phrase[:-2]    # All but the last two characters


# But note that -0 is really the same as 0, so it does not count from the right! 

print phrase[-0]     # (since -0 equals 0)

# Out-of-range negative slice indices are truncated, but don't try this for single-element (non-slice) indices: 

print phrase[-100:]

# print phrase[-10]    # error

#The best way to remember how slices work is to think of the indices as pointing between characters, 
#with the left edge of the first character numbered 0. Then the right edge of the last character 
#of a string of n characters has index n, for example: 


s = 'Internet of Things and the Future Internet'
print s
print len(s)
