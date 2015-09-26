import sys

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <input> <output>")
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: x,1).reduce(lambda x,y:x+y)
    counts.saveAsTextFile(sys.argv[2])
    sc.stop()
