'''
Created on Aug 7, 2016

@author: james
'''

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

x = tf.placeholder('float', [None, 784])
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder('float', [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

num_steps = 1000
batch_size = 100
for i in range(num_steps):
    # Training
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})
    
    # Evaluation
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
    #print('Accuracy : ', sess.run(accuracy, feed_dict={x:mnist.test.images, y_:mnist.test.labels}))
    
print('Accuracy : ', sess.run(accuracy, feed_dict={x:mnist.test.images, y_:mnist.test.labels}))    
    