########How to Run Basic Programs#########
# a = 2

# print( a )

# print( a * 5 )



###################Basic Command Lines##############

# Directory -> Folder

# 1) cd -> change directory
        # Ex :- cd C:\Users\gauta\Downloads\eclipse

    # a) Got back to previous directory
    # Ex :- cd ../

# 2) pwd -> present working directory/ present current directory
        # Ex :- C:\Users\gauta\Downloads\eclipse>pwd
            #   /c/Users/gauta/Downloads/eclipse

# 3) ls -> list all the items in the present directory
    # Ex :- C:\Users\gauta\Downloads\eclipse>ls
        # artifacts.xml  configuration  dropins  eclipse.exe  eclipse.ini  eclipsec.exe  features  p2  plugins  readme

# 4) ls -lrt -> This will show you the permission, time stamp, user_details, file-size, file/foldername
    # Ex :-
    # C:\Users\gauta\Downloads\eclipse>ls -lrt
    # drwxr-xr-x 1 gauta 197609      0 Mar 14  2017 features
    drwxr-xr-x 1 gauta 197609      0 Mar 14  2017 plugins
    -rw-r--r-- 1 gauta 197609 178690 Mar 14  2017 artifacts.xml
    drwxr-xr-x 1 gauta 197609      0 Mar 14  2017 readme
    -rw-r--r-- 1 gauta 197609    478 Mar 14  2017 eclipse.ini
    drwxr-xr-x 1 gauta 197609      0 Mar 14  2017 dropins
    -rwxr-xr-x 1 gauta 197609  25584 Mar 14  2017 eclipsec.exe
    -rwxr-xr-x 1 gauta 197609 319984 Mar 14  2017 eclipse.exe
    drwxr-xr-x 1 gauta 197609      0 Nov 29 09:02 configuration
    drwxr-xr-x 1 gauta 197609      0 Nov 29 09:02 p2

    C:\Users\gauta\Downloads\eclipse>

# 5) mkdir -> make directory/ make folder
    # Ex :-
    # gauta@LAPTOP-MLRCJ715 MINGW64 ~/Desktop
    # $ mkdir epam_training


# 6) touch -> To create a file
    # tocuh file_name.extention
    # Ex :- touch message.txt


# 7) less file_name -> Shows the content of file
    # Ex :- $ less message.txt
    # "Hello EPAM TEAM"

# 8) echo -> It's like a print
    # echo "Hello"

# 9) echo -> echo "Hello" > message.txt -> Remove the old one and write the new one
    # echo -> echo "Hello" >> message.txt -> append the data in the file

# 10) cp -> copy
    # cp source destination
    # $ cp message.txt message_backup.txt

    # $ cp message.txt ../

# 11) mv
    # a) rename the file
        # mv curr_file_name  new_file_name

        Ex :-
        gauta@LAPTOP-MLRCJ715 MINGW64 ~/Desktop/epam_training
        $ ls -lrt
        total 2
        -rw-r--r-- 1 gauta 197609 42 Mar  7 10:25 message_backup.txt
        -rw-r--r-- 1 gauta 197609  6 Mar  7 10:26 message.txt

        gauta@LAPTOP-MLRCJ715 MINGW64 ~/Desktop/epam_training
        $ mv message.txt info.txt

        gauta@LAPTOP-MLRCJ715 MINGW64 ~/Desktop/epam_training
        $ ls -lrt
        total 2
        -rw-r--r-- 1 gauta 197609 42 Mar  7 10:25 message_backup.txt
        -rw-r--r-- 1 gauta 197609  6 Mar  7 10:26 info.txt

    # b) move the file( cut and paste )

    # mv curr_file_name new_directory

# 12) rm -> remove
    # rm file_name


 




