#!/bin/bash
MYSQL_USER=insert_user_name
MYSQL_PASS=inser_password
MYSQL_SO_DB=insert_database_name

echo "Creating CSV files  (be patient, this also takes a while...)"
mysql -u "$MYSQL_USER" --password="$MYSQL_PASS" --database="$MYSQL_SO_DB" < csv.sql
echo "done".
