from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import matplotlib.pyplot as plt 

#Loads data.
dataset = spark.read.format("libsvm").load("data/mlib/sample_kmeans_data.txt")

#Train a k-means model.
kmeans = KMeans().setk(2).setSeed(1)
model = kmeans.fit(dataset)

#make predictions
predictions = model.transform(dataset)

#convert to panda dataframe
pdf = predictions.toPandas()

#Plot the data points and their cluster labels
plt.scatter(pdf['features'].apply(lambda x: x[0]),pdf['features'].apply(lambda x: x[1]),
            c = pdf['prediction'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.show()