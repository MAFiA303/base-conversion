# base-conversion
change numbers between different bases
newbase(number,old base, new base)
example: Change number 303 from base 10 to base 2

newBase(303,10,2)
output is a string:
>> '100101111'

use minBase to find the minimum base the input can be at, ex:
maf.minBase('saad')
>> 29
maf.newBase('saad',29,2)
>> '10101000110110010101'
