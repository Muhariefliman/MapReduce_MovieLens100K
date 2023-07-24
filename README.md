# MapReduce_MovieLens100K
Group Project For Map Reduce using Movie Lens Dataset

How To Run:
#run locallly

#u.data is the dataset.


python mapreduce.py u.data


#run with hadoop

#python [python file] -r hadoop --hadoop-streaming-jar [The_path_of_Hadoop_Streaming_jar] [dataset]


python mapreduce.py -r hadoop --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1 jar u.data
