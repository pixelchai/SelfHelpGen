# To be run in Colab notebook:

import zipfile

# extract training data
with zipfile.ZipFile("data.zip", "r") as fh:
    fh.extractall()

import os
from textgenrnn import textgenrnn as Gen

WEIGHTS_PATH = "model.hdf5"
gen = Gen(WEIGHTS_PATH if os.path.isfile(WEIGHTS_PATH) else None)

try:
    gen.train_from_file("data.txt", num_epochs=1)
finally:
    gen.save(WEIGHTS_PATH)
