
#!/bin/bash

for v in $@
do 
    echo $v
done
 
egrepColor="egrep --color=always -i"


GREP_COLOR='31' $egrepColor 'red|' test.log |\
GREP_COLOR='32' $egrepColor 'green|' 


#GREP_COLOR='31' $egrepColor 'red' test.log #red
#GREP_COLOR='32' $egrepColor 'green' test.log #green
#GREP_COLOR='33' $egrepColor 'yellow' test.log #yellow
#GREP_COLOR='34' $egrepColor 'blue' test.log #blue
#GREP_COLOR='35' $egrepColor 'magenta' test.log #magenta
#GREP_COLOR='36' $egrepColor 'cyan' test.log #cyan
#GREP_COLOR='4;31' $egrepColor 'redu' test.log #red underline
#GREP_COLOR='4;32' $egrepColor 'greenu' test.log #green underline
#GREP_COLOR='4;33' $egrepColor 'yellowu' test.log #yellow underline
#GREP_COLOR='4;34' $egrepColor 'blueu' test.log #blue underline
#GREP_COLOR='4;35' $egrepColor 'magentau' test.log #magenta underline 
#GREP_COLOR='4;36' $egrepColor 'cyanu' test.log #cyan underline
#GREP_COLOR='4' $egrepColor 'underline' test.log #underline

