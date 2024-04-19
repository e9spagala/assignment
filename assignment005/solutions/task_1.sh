head -n 1 test_data.csv  > sliced.csv

head -n 843 test_data.csv | tail -n +13  >> sliced.csv
