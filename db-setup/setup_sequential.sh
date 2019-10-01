#!/bin/bash
MYSQL_USER=insert_user_name
MYSQL_PASS=insert_password
MYSQL_SO_DB=insert_database_name

echo "Creating tables and indexes (be patient, it does take a while...)"
mysql -u "$MYSQL_USER" --password="$MYSQL_PASS" --database="$MYSQL_SO_DB" < setup.sql

echo "done."
