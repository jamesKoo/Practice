'''
Created on Jul 30, 2016

@author: james
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf


# Create sample data
num_points = 2000
conjunto_points = []

for i in range(num_points):
    if np.random.random() > 0.5:
        conjunto_points.append([np.random.normal(0.0, 0.9), np.random.normal(0.0, 0.9)])
    else:
        conjunto_points.append([np.random.normal(3.0, 0.5), np.random.normal(1.0, 0.5)])

df = pd.DataFrame({'x': [v[0] for v in conjunto_points], 'y':[v[1] for v in conjunto_points]})
sns.lmplot('x', 'y', data=df, fit_reg=False, size=6)


# Calculate distance and assignments
vectors = tf.constant(conjunto_points)
k = 4
centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors), [0, 0], [k, -1]))

expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroides = tf.expand_dims(centroides, 1)

diff = tf.sub(expanded_vectors, expanded_centroides)
sqr = tf.square(diff)
distances = tf.reduce_sum(sqr, 2)
assignments = tf.argmin(distances, 0)

# Calculate means of clusters
means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where( tf.equal(assignments, c)),[1,-1])), reduction_indices=[1]) for c in range(k)])
update_centroides = tf.assign(centroides, means)

''' Step by step for means of clusters

means = tf.Variable(tf.zeros([0,2]))

for c in range(k) :
    assignments_equal = tf.equal(assignments, c)
    assignments_coord = tf.where(assignments_equal)
    assignments_reshape = tf.reshape(assignments_coord, [1, -1])
    vectors_in_c = tf.gather(vectors, assignments_reshape)
    mean_in_c = tf.reduce_mean(vectors_in_c, reduction_indices = [1])
    means = tf.concat(0, [means, mean_in_c])
         
print("assignments_reshape = " , assignments_coord)
print("assignments_reshape = " , assignments_reshape)
print("vectors_in_c = " , vectors_in_c)
print("mean_in_c = " , mean_in_c)
print("means =" , means)

'''

# Initialize tensforFlow
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# Iterate update centroides
num_steps = 1000
for step in range(num_steps):
    _, centroid_values, assignment_values = sess.run([update_centroides, centroides, assignments])
 
    
# Show centroides and a graph of results.
print(centroid_values)

data = {'x' : [], 'y' : [], 'cluster': []}

for i in range(len(assignment_values)):
    data['x'].append(conjunto_points[i][0])
    data['y'].append(conjunto_points[i][1])
    data['cluster'].append(assignment_values[i])
    
df = pd.DataFrame(data)
sns.lmplot('x', 'y', data=df, fit_reg=False, size=6, hue='cluster', legend=False)
plt.show()




