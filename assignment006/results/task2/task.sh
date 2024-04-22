
OPFILE="./asia_sale.csv"
# add the headers to the op file
echo "Region,Country,Total Revenue,Total Cost,Total Profit" > $OPFILE

# find the files that contains Sales through find command
sales_files=$(find ../../test_data/ -type f -name "*Sales*")

# for every file that has Sales as a keyword bring 1,2,12,13,14 columns.
for i in $sales_files
do
    awk -F, '$1=="Asia" {print $1,$2,$12,$13,$14}' $i
done > $OPFILE
