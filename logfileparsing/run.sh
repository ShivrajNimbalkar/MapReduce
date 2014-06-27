
# copy log data file to HDFS
hadoop fs -put data/access_log logdata

echo "Copied data file to HDFS. Starting MapReduce..."

# Run MapReduce
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.7.0.jar -mapper code/mapper.py -reducer code/reducer.py -file code/mapper.py -file code/reducer.py -input logdata -output logout

