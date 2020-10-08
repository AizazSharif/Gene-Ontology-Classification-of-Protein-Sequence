config = {}
class TrainingConfig(object):

    p = 0.5
    base_rate = 1e-2
    momentum = 0.9
    decay_step = 1500
    decay_rate = 0.95
    epoches = 1000
    evaluate_every = 100
    checkpoint_every = 100

class ModelConfig(object):
    conv_layers = [[256, 7, 3],
                   [256, 7, 3],
                   [256, 3, None],
                   [256, 3, None],
                   [256, 3, None],
                   [256, 3, 3]]

    fully_connected_layers = [250, 200]
    th = 1e-6
    
    
class Config(object):

    alphabet = ['_', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    alphabet_size = len(alphabet)
    l0 = 200
    batch_size = 512
    no_of_classes = 21

    train_data_source = 'data/dataset/train.csv'
    dev_data_source = 'data/dataset/test.csv'
    
    training = TrainingConfig()
    
    model = ModelConfig()

config = Config()
