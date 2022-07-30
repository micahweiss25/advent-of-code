from MyProgram import NeuralNetwork, Layer
from keras.datasets import mnist

(train_X, train_y), (test_X, test_y) = mnist.load_data()

model = NeuralNetwork()

model.addLayer(activation="sigmoid", nodes=16, input_size=716)
model.addLayer(activation="sigmoid", nodes=32, input_size=16)

print('X_train: ' + str(train_X.shape))
'''print('Y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('Y_test:  '  + str(test_y.shape))'''
#print(model)

data = []
for i in train_X[:10]:
    for j in i:
        for k in j:
            data.append(k)
#print(data)
model.run(train_X[:10])