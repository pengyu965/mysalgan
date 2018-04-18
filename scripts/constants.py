# Work space directory
HOME_DIR = '/imatge/jpan/saliency-salgan-2017/'

# Path to SALICON raw data
pathToImages = './images'
pathToMaps = './saliency'
pathToFixationMaps = './salicon_data/fixation'

# Path to processed data
pathOutputImages = './lsun2016/data/salicon/images320x240'
pathOutputMaps = './lsun2016/data/salicon/saliency320x240'
pathToPickle = './scratch-local/salicon_data/320x240'

# Path to pickles which contains processed data
TRAIN_DATA_DIR = './scratch-local/salicon_data/320x240/fix_trainData.pickle'
VAL_DATA_DIR = './scratch-local/salicon_data/320x240/fix_validationData.pickle'
TEST_DATA_DIR = './scratch-local/salicon_data/256x192/testData.pickle'

# Path to vgg16 pre-trained weights
PATH_TO_VGG16_WEIGHTS = '/imatge/jpan/saliency-salgan-2017/vgg16.pkl'

# Input image and saliency map size
INPUT_SIZE = (256, 192)

# Directory to keep snapshots
DIR_TO_SAVE = 'test'
