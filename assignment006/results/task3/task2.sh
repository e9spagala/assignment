OPFILE="task3_output.txt"
RDFILE="task3_data.txt"

read -p "please enter a number: " n
i=0

while IFS= read -r line
do
    if (( i % n == 0 ))
    then
        echo $line
    fi
    (( ++i ))
done < $RDFILE > $OPFILE

