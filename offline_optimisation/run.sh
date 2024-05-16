#!/bin/bash

PROJECT_PATH="/home/manospits/projects/onfore/"
WAYEB_JAR="libraries/models/wrappers/wayeb/target/scala-2.12/wayeb-0.3.0-SNAPSHOT.jar"
WAYEB_PATH=$(echo $PROJECT_PATH$WAYEB_JAR)



java -jar ${PROJECT_PATH}${WAYEB_JAR} server > wayeb_server_print_log.log 2>&1 & PID_WSS=("$!")
echo $PID_WSS > wayeb_server_pid.txt

python optimise_wayeb.py
