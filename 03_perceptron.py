class Perceptron(object):
    def __init__(self, input_num, activator):
        '''
        初始化感知器，設置輸入參數的個數，以及啟動函數。
        啟動函數的類型為double -> double
        '''
        self.activator = activator
        # 權重向量初始化為0
        self.weights = [0.0 for _ in range(input_num)]
        # 偏置項初始化為0
        self.bias = 0.0

    def __str__(self):
        '''
        列印學習到的權重、偏置項
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def predict(self, input_vec):
        '''
        輸入向量，輸出感知器的計算結果
        '''
        # 把input_vec[x1,x2,x3...]和weights[w1,w2,w3,...]打包在一起
        # 變成[(x1,w1),(x2,w2),(x3,w3),...]
        # 然後利用map函數計算[x1*w1, x2*w2, x3*w3]
        # 最後利用reduce求和
        return self.activator( 
            reduce(lambda a, b: a + b, 
                   map( lambda (x, w): x * w, zip(input_vec, self.weights) ), 
                   0.0) + self.bias
            )

    def train(self, input_vecs, labels, iteration, rate):
        '''
        輸入訓練資料：一組向量、與每個向量對應的label；以及訓練輪數、學習率
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        '''
        一次反覆運算，把所有的訓練資料過一遍
        '''
        # 把輸入和輸出打包在一起，成為樣本的清單[(input_vec, label), ...]
        # 而每個訓練樣本是(input_vec, label)
        samples = zip(input_vecs, labels)
        # 對每個樣本，按照感知器規則更新權重
        for (input_vec, label) in samples:
            # 計算感知器在當前權重下的輸出
            output = self.predict(input_vec)
            # 更新權重
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        '''
        按照感知器規則更新權重
        '''
        # 把input_vec[x1,x2,x3,...]和weights[w1,w2,w3,...]打包在一起
        # 變成[(x1,w1),(x2,w2),(x3,w3),...]
        # 然後利用感知器規則更新權重
        delta = label - output
        self.weights = map(
            lambda (x, w): w + rate * delta * x,
            zip(input_vec, self.weights))
        # 更新bias
        self.bias += rate * delta

def f(x):
    '''
    定義啟動函數f
    '''
    return 1 if x > 0 else 0

def get_and_training_dataset():
    '''
    基於and真值表構建訓練資料
    '''
    # 構建訓練數據
    # 輸入向量列表
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    # 期望的輸出列表，注意要與輸入一一對應
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 0, 0] #AND
    return input_vecs, labels   

def get_or_training_dataset():
    '''
    基於and真值表構建訓練資料
    '''
    # 構建訓練數據
    # 輸入向量列表
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    # 期望的輸出列表，注意要與輸入一一對應
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 1, 1] #OR
    return input_vecs, labels   
 
def train_and_perceptron():
    '''
    使用and真值表訓練感知器
    '''
    # 創建感知器，輸入參數個數為2（因為and是二元函數），啟動函數為f
    p = Perceptron(2, f)
    # 訓練，反覆運算10輪, 學習速率為0.1
    input_vecs, labels = get_and_training_dataset()
    
    # 期望的輸出列表，注意要與輸入一一對應
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    p.train(input_vecs, labels, 10, 0.01)
    #返回訓練好的感知器
    return p

def train_or_perceptron():
    '''
    使用and真值表訓練感知器
    '''
    # 創建感知器，輸入參數個數為2（因為and是二元函數），啟動函數為f
    p = Perceptron(2, f)
    # 訓練，反覆運算10輪, 學習速率為0.1
    input_vecs, labels = get_or_training_dataset()
    
    # 期望的輸出列表，注意要與輸入一一對應
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    p.train(input_vecs, labels, 10, 0.01)
    #返回訓練好的感知器
    return p

if __name__ == '__main__': 

    print'================================'
    print 'AND operator'
    # 訓練and感知器
    and_perception = train_and_perceptron()
    # 列印訓練獲得的權重
    print and_perception
    # 測試
    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '1 and 0 = %d' % and_perception.predict([1, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])

    print'================================'
    print 'OR operator'
    or_perception = train_or_perceptron()
    # 列印訓練獲得的權重
    print or_perception
    # 測試
    print '1 and 1 = %d' % or_perception.predict([1, 1])
    print '0 and 0 = %d' % or_perception.predict([0, 0])
    print '1 and 0 = %d' % or_perception.predict([1, 0])
    print '0 and 1 = %d' % or_perception.predict([0, 1])
    print'================================'
