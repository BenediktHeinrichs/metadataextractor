#! /bin/sh
if [ ! -f ./tika-server.jar ]
then
    wget -O ./tika-server.jar https://dlcdn.apache.org/tika/2.7.0/tika-server-standard-2.7.0.jar
fi
java -jar ./tika-server.jar &
python ./server.py
