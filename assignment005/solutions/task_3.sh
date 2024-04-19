echo "enter n:"
read n


# length of arr = ${#a[@]}


factorial=(1 1)

    for (( i=0; i < n; ++ i ))
    do
        if [[ n > 1 ]]
        then
            factorial+=(${factorial[i - 1]}*$i)
        fi
        echo $i,${factorial[i]}
    done > result.txt