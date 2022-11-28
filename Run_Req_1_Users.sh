#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
export HADOOP_HOME=/home/hadoop/hadoop
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*

echo "                            _______________________________                            "
echo "***************************|                               |***************************"
echo "***************************|  Starting Requirment 1 Codes  |***************************"
echo "***************************|_______________________________|***************************"
echo "                                                                                       "  

input="Req_1/Task_Users"
input_file="test.txt"
FirstOutput="FirstOutput.txt"
FinalOutput="FinalOutput.txt"
output="/Req_1_Users_Out"

mappers=5
reducers=1
hadoop fs -rm -r $input


hadoop fs -mkdir -p $input
hadoop fs -put $input_file $input/$input_file
hadoop fs -rm -r $output

hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
    -file T2_Mapper1.py -mapper 'T2_Mapper1.py' \
    -file T2_Reducer1.py -reducer 'T2_Reducer1.py' \
    -input $input/$input_file \
    -output $output \


hadoop fs -text "$output/part-00000" >> $input/$FirstOutput

hadoop fs -rm -r $output
hadoop fs -put $FirstOutput $input/ 

hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
     -file $input/T2_Mapper2.py -mapper 'T2_Mapper2.py' \
     -file $input/T2_Combiner2.py -combiner 'T2_Combiner2.py' \
     -file $input/T2_Reducer2.py -reducer 'T2_Reducer2.py' \
     -input $input/$FirstOutput \
     -output $output

hadoop fs -text "$output/part-00000" >> $input/$FinalOutput
