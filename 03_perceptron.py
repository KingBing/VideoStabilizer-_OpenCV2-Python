class Perceptron(object):
    def __init__(self, input_num, activator):
        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0

    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def predict(self, input_vec):
        return self.activator( 
            reduce(lambda a, b: a + b, 
                   map( lambda (x, w): x * w, zip(input_vec, self.weights) ), 
                   0.0) + self.bias
            )

    def train(self, input_vecs, labels, iteration, rate):
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        samples = zip(input_vecs, labels)
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        delta = label - output
        self.weights = map(
            lambda (x, w): w + rate * delta * x,
            zip(input_vec, self.weights))
        self.bias += rate * delta

def f(x):
    return 1 if x > 0 else 0

def get_and_training_dataset():
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1, 0, 0, 0] #AND
    return input_vecs, labels   

def get_or_training_dataset():
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1, 0, 1, 1] #OR
    return input_vecs, labels   
 
def train_and_perceptron():
    p = Perceptron(2, f)
    input_vecs, labels = get_and_training_dataset()
    p.train(input_vecs, labels, 10, 0.01)
    return p

def train_or_perceptron():
    p = Perceptron(2, f)
    input_vecs, labels = get_or_training_dataset()
    p.train(input_vecs, labels, 10, 0.01)

    return p

if __name__ == '__main__': 

    print'================================'
    print 'AND operator'
    and_perception = train_and_perceptron()
    
    print and_perception

    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '1 and 0 = %d' % and_perception.predict([1, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])

    print'================================'
    print 'OR operator'
    or_perception = train_or_perceptron()
    
    print or_perception
    
    print '1 and 1 = %d' % or_perception.predict([1, 1])
    print '0 and 0 = %d' % or_perception.predict([0, 0])
    print '1 and 0 = %d' % or_perception.predict([1, 0])
    print '0 and 1 = %d' % or_perception.predict([0, 1])
    print'================================'
