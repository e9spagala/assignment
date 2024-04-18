# Basic linux commands:

1. use `cd`, `mkdir`, `touch` to complete the first assignment and use `tree` command to list out the dir structure in tree format
  ![creating basic folder structure-1](https://github.com/e9spagala/assignment/assets/167054006/3fafb2e4-d273-42d3-9d3a-7060501ebcf0)
![basic folder structure - 2](https://github.com/e9spagala/assignment/assets/167054006/571a6adb-8628-4b6d-aac7-a2d8d0353873)
![files in 7](https://github.com/e9spagala/assignment/assets/167054006/6d4a3e50-0743-464a-85af-03ce5745e1fa)

![basic structure](https://github.com/e9spagala/assignment/assets/167054006/b56f0890-476a-4c03-8a3e-b07475414a04)


2. List all csv files:

use `find` command to get the files ending with the extension `.csv`

![csv files list](https://github.com/e9spagala/assignment/assets/167054006/96cced1a-1982-4078-af2e-cfb3b2fe127e)


3. Find the number of ".pdf" files in base_dir

- You can find the number of `.pdf` files by piping the `find -type f -name *.pdf` to `wc -l` which gives number of lines as output
  
![pdf files num](https://github.com/e9spagala/assignment/assets/167054006/543bbb15-ae8b-4c94-b193-8942642e03d3)


4. Create a "results" directory on the same level as base_dir

![make results](https://github.com/e9spagala/assignment/assets/167054006/0459dd11-7abe-4c9f-82fd-2a9afc31327d)




5. Create a file "filename_7_dup.txt", in the results directory, which should have all the content from "filename_7.txt".

- use `cat` command or `cp` command 

![move contents of file 7 to the results](https://github.com/e9spagala/assignment/assets/167054006/139ec854-28d1-47e1-b242-dc55b16ef4c3)


6. Append the content of files filename_1.csv, filename_3.csv, filename_5.csv and store the output at "/results/combined.csv"

- use `cat` command and then stream the output in append mode to the required file

![append 3 files](https://github.com/e9spagala/assignment/assets/167054006/c319fa84-7cf0-4562-b0ec-cf4c66ca9e9c)


7. Shift the folder "dir_6" to the "results" folder.
I like to use `copy-delete` strategy instead of using `mv` as it reduces ambiguity

![move dir_6 to results](https://github.com/e9spagala/assignment/assets/167054006/a525f6c4-bd4f-4905-9d8d-3f1ecbd6ca6d)

8. Search for a keyword in the files in base_dir.

    1. Find the number of occurrences of the keyword.
       - use grep and then use `--only-matching` or `-o` to print only the matching part. then pipe it to `wc - l` which counts the number of lines
       
       ![number of occurances of keyword](https://github.com/e9spagala/assignment/assets/167054006/45517118-0568-40b2-bf3f-eaf5d4951bd6)

      
       
    2. Print all lines containing that keyword
  
       ![all the line containing keyword](https://github.com/e9spagala/assignment/assets/167054006/6f335e38-3cae-493d-8f99-4ad57d681e8f)
    
    
    3. Print all the content in the files that did
 not have the searched keyword.
  - use `-v` to invert the match

    ![all-lines-not-keyword](https://github.com/e9spagala/assignment/assets/167054006/d557ddde-25e9-42e7-a7c5-d8fff44822e4)

9. List all the files present in the results directory.
 
 ![listing results](https://github.com/e9spagala/assignment/assets/167054006/35a1d156-718f-4c51-9a12-4b00c72c9d2a)


