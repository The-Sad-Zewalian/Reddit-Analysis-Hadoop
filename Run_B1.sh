#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
export HADOOP_HOME=~/hadoop
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}

echo "                            _______________________________                            "
echo "***************************|                               |***************************"
echo "***************************|  Starting Bonus Idea 1 Codes  |***************************"
echo "***************************|_______________________________|***************************"
echo "                                                                                       "  

#params of job
prefix='Bonus_Ideas/B1'
input_file="test.txt"
mappers=5
output="B1_Out"
reducers=1

#delete old dirs 
echo "                                                                                       "
echo "Deleting Old Folders To Start..........................."
echo "                                                                                       "
hadoop fs -rm -R $prefix
hadoop fs -rm -R $output

echo "                                                                                       "
echo "Creating input and file Folders To Start..........................."
echo "                                                                                       "

#make new dirs and move the files needed
hadoop fs -mkdir "Bonus_Ideas"
hadoop fs -mkdir $prefix
hadoop fs -put $prefix/* $prefix

echo "                            _______________________________                            "
echo "***************************|                               |***************************"
echo "***************************|Intiating Hadoop El Dapdoop Job|***************************"
echo "***************************|_______________________________|***************************"
echo "                                                                                       "

#start the hadoop job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar  -D mapred.map.tasks=$mappers -D mapred.reduce.tasks=$reducers\
    -files $prefix/mapper.py,$prefix/reducer.py,$prefix/combiner.py \
    -input $input_file \
    -output $output \
    -mapper mapper.py\
    -reducer reducer.py \
    -combiner combiner.py

#print the output
echo "                                                                                               "
echo "Printing Output..............................."
echo "                                                                                               "
hadoop fs -text "$output/part-00000"