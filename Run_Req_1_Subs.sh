#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
export HADOOP_HOME=/home/hadoop/hadoop
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*

echo "                            _______________________________                            "
echo "***************************|                               |***************************"
echo "***************************|  Starting Requirment 1 Task 1 |***************************"
echo "***************************|__________Subreddits___________|***************************"
echo "                                                                                       "  

prefix="Req_1/Task_Subreddits"
input_file="test.txt"

FirstOutput="FirstOutput.txt"
FinalOutput="FinalOutput.txt"

output1="Req_1_Subreddits_Out1"
output="Req_1_Subreddits_Out"

mappers=5
reducers=1


#delete old dirs 
echo "                                                                                       "
echo "Deleting Old Folders To Start..........................."
echo "                                                                                       "
hadoop fs -rm -R $prefix
hadoop fs -rm -R $output1
hadoop fs -rm -R $output

echo "                                                                                       "
echo "Creating input and file Folders To Start..........................."
echo "                                                                                       "

#make new dirs and move the files needed
hadoop fs -mkdir "Req_1"
hadoop fs -mkdir $prefix
hadoop fs -put $prefix/* $prefix

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar  -D mapred.map.tasks=$mappers -D mapred.reduce.tasks=$reducers \
    -files $prefix/T1_Mapper1.py,$prefix/T1_Reducer1.py \
    -input $input_file \
    -output $output1 \
    -mapper T1_Mapper1.py \
    -reducer T1_Reducer1.py 


hadoop fs -text "$output1/part-00000" >> $prefix/$FirstOutput

echo "                            _______________________________                            "
echo "***************************|                               |***************************"
echo "***************************|  Starting Requirment 1 Task 2 |***************************"
echo "***************************|__________Subreddits___________|***************************"
echo "                                                                                       "  

hadoop fs -put $prefix/$FirstOutput $prefix

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar  -D mapred.map.tasks=$mappers -D mapred.reduce.tasks=$reducers \
     -files $prefix/T1_Mapper2.py,$prefix/T1_Combiner2.py,$prefix/T1_Reducer2.py \
     -mapper T1_Mapper2.py \
     -combiner T1_Combiner2.py \
     -reducer T1_Reducer2.py \
     -input $prefix/$FirstOutput \
     -output $output

hadoop fs -text "$output/part-00000" >> $prefix/$FinalOutput
