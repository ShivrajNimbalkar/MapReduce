
#create directory to put data
hadoop fs -mkdir /tablesdata

# copy table data file to HDFS
hadoop fs -put data/records.json /tablesdata

echo "Copied data file to HDFS. Starting MapReduce..."

# Run MapReduce
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.4.0.jar -file code/mapper.py -mapper code/mapper.py -file code/reducer.py -reducer code/reducer.py -input /tablesdata -output tablejoinout


