import sys
import re

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <input> <output>")
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    common_words = ["the", "a", "an", "and", "of", "to", "in", "am", "is", "are", "at", "not"]
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: re.split(r"[ \t,;\.\?!:@\[\]\(\){}_\*/]+",x))\
        .filter(lambda x: x.lower() not in common_words and
                          len(x) > 0)\
        .map(lambda x: (x, 1))\
        .reduceByKey(lambda a,b : a+b)
    counts.saveAsTextFile(sys.argv[2])
    sc.stop()
