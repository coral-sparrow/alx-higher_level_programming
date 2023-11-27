#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.index('ob'):str.index(' l')], end = ' ')
print(str[str.index('with'):str.index('with') + 4], str[:7], sep = ' ')
