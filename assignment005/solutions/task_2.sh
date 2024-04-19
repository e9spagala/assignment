
echo 'please enter n: ';
read n 


a=0
b=1

if [[ $n == 0 ]]
then
   echo "0"
elif [[ $n == 1 ]]
then
   echo "1"
else
    c=1
   for i in $(seq 2 $n)
    do
        c=$((a+b))
        b=$a
        a=$c
    done
    echo "the $n th fibonacii is $c"
fi