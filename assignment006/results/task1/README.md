## For loop

syntax:

```
for var in word1 word2 ... wordN
do
   Statement(s) to be executed for every word.
done
```

Iterating over 1 to 10 digits

```bash
for i in {1..10}
do
  echo $i
done
```

output:

```
1
2
3
4
5
6
7
8
9
10
```

Iterating over an array:
- elements are space seperated.

```bash
declare -a list=(1 2 3 4 5)
for i in "${list[@]}"
do
  echo $i
done
```
output:
```
1
2
3
4
5
```

- We can use normal iteration like shown below

```bash

for ((i=0; i < 10; ++ i))
do
  echo $i
done
```

output:

```
0
1
2
3
4
5
6
7
8
9
```

## cut command
cut command is used to cut the sections from each line of files and writing the result.
It can cut the line byte by byte position, character or a field
syntax:
cut OPTION... [FILE]...

`-d` is used for delimiter
`-f` is used for field
`-c` is used for character
`--complement` will invert the result

specifing characters `cut -c 1,2,3,4,5,9,10 filename` 
specifing range of characters `cut -c 1-10 filename` 
cut by field `cut -f 1 filename`
cut by field seperated by delimiter `cut -d " "  -f 1 filename`

## awk command

- awk command is used to extract the lines satisfying the condition
- we can write internal logic in awk
syntax:
awk options 'selection _criteria {action }' input-file > output-file

- awk with fields with seperator as `,` and a condition that the first field is asia and only print 1,2,12,13,14 fields data.

```
    awk -F, '$1=="Asia" {print $1,$2,$12,$13,$14}' $i
```

## loops in awk

```
# for loop
awk 'BEGIN { for (i = 1; i <= 5; ++i) print i }'
#while loop
awk 'BEGIN {i = 1; while (i < 6) { print i; ++i } }'
```
> note: use double quotes while using external variables.


## NR

nr command basically used to count the number of lines in awk

```
awk 'BEGIN{print "Line", "\tCount"}{print NR "\t" gsub(/E/,"")}' file_name
```



## references

[for loop by hackerexploit](https://www.youtube.com/watch?v=T7hVOiTsSUU&t=497s)
[arrays in unix](https://www.youtube.com/watch?v=x3jGq524vBA)
[awk and cut commands](https://www.youtube.com/watch?v=dcF5Rqw_VZ4)
