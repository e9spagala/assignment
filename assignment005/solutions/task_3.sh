echo "enter n:"
read n


# length of arr = ${#a[@]}


fact=1
i=0
while (($i <= $n)) 
do
    echo $i,$fact
    ((++ i))
    fact=$((fact * i))
done > result.txt