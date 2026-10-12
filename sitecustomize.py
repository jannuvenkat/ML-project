
import sys
import types
from keras.utils import to_categorical

np_utils = types.ModuleType("keras.utils.np_utils")
np_utils.to_categorical = to_categorical
sys.modules["keras.utils.np_utils"] = np_utils
