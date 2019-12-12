#!/bin/bash
MYSQL_USER=user_name
MYSQL_PASS=password
MYSQL_SO_DB=database_name

echo "Creating tables and indexes (be patient, it does take a while...)"
mysql -u "$MYSQL_USER" --password="$MYSQL_PASS" --database="$MYSQL_SO_DB" < setup.sql

echo "done."
