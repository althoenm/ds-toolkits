from sklearn.cluster import KMeans
wcss = []

#Get WCSS scores for 1-10 clusters
for i in range(1, 11): #1-10 clusters
    '''
    Kmeans++ avoids random initialization trap
    Random state can be any number. Use for fixed results
    '''
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
#Plot results
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()