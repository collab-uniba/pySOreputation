#!/bin/bash
MYSQL_USER=username
MYSQL_PASS=password
MYSQL_SO_DB=database-name
MYSQL_SO_FOLDER=/path/to/mysql-data-dir/$MYSQL_SO_DB

echo "Creating CSV files into folder $MYSQL_SO_FOLDER (be patient, this takes a while...)"
mysql -u "$MYSQL_USER" --password="$MYSQL_PASS" --database="$MYSQL_SO_DB" < csv.sql

echo "Moving CSV files to proper destinations (for both CLI client and web service server)"
mv $MYSQL_SO_FOLDER/*.csv ../parallel 
ln -s ../parallel_version/Users.csv ../SOWebService/Users.csv
ln -s ../parallel_version/Question_Answer.csv ../SOWebService/Question_Answer.csv
ln -s ../parallel_version/Posts_Votes1.csv ../SOWebService/Posts_Votes1.csv
ln -s ../parallel_version/Posts_Votes2.csv ../SOWebService/Posts_Votes2.csv
ln -s ../parallel_version/Posts_Votes3.csv ../SOWebService/Posts_Votes3.csv
ln -s ../parallel_version/Posts_Votes4.csv ../SOWebService/Posts_Votes4.csv

echo "Done."
