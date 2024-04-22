OPFILE="task3_data.txt"
LIMIT=400000

# for i in {1..400000}
# do
#     echo "This is line no "$i
# done > $OPFILE

awk "BEGIN {while(i<$LIMIT){++i; print \"This is line no \" i}}" > $OPFILE