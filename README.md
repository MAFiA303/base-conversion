# base-conversion
change numbers between different bases
```python
newbase(number,old base, new base,case senitive bool)
```
###### example: Change number 303 from base 10 to base 2

```python
newBase(303,10,2)
'100101111'
```

###### use minBase to find the minimum base the input can be at, ex:
```python
minBase('saad')
29
newBase('saad',29,22)
'2kkkd'
```

## Cyphering options:

###### Change a word to ascii
```python
text2asc('MAFiA')
'077065070105065'
```
###### Change output to a new base
```python
maxBase
93
newBase('077065070105065',10,93)
'1qaN4<KB'
```
##### Decypher
```python
newBase('1qaN4<KB',93,10,True)
77065070105065
asc2text(77065070105065)
'MAFiA'
```
