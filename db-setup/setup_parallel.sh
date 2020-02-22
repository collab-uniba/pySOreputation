#!/bin/bash
MYSQL_USER=username
MYSQL_PASS=password
MYSQL_SO_DB=database-name
MYSQL_SO_FOLDER=/path/to/mysql-data-dir/$MYSQL_SO_DB

echo "Creating CSV files into folder $MYSQL_SO_FOLDER (be patient, this takes a while...)"
mysql -u "$MYSQL_USER" --password="$MYSQL_PASS" --database="$MYSQL_SO_DB" < csv.sql

echo "Moving CSV files to proper destinations (for both CLI client and web service server)"
mv $MYSQL_SO_FOLDER/*.csv ../parallel 

echo "Done."
