import mne
import os
import scipy.io
dataset_dir = f"{os.path.dirname(__file__)}/datasets"
dataset = scipy.io.loadmat(f"{dataset_dir}/CLA-SubjectJ-170508-3St-LRHand-Inter.mat")
daneDlaMNE = mne.io.read_raw_fif(dataset, preload=True)
print(dataset)
# daneDlaMNE.plot_psd()

