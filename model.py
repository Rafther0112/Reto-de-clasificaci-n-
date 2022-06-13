#%%
import pickle
import numpy as np
from skimage import img_as_float
#%%
def Model():
    with open("mejor_modelo_entrenado.json", "rb") as modelo:
        modelo = pickle.load(modelo)
    return modelo
#%%
def Descriptor():
    with open("descriptor_final.json", "rb") as modelo:
        final = pickle.load(modelo)
        descriptor = final["Descriptores"]
        anotaciones = final["Label"]
    return descriptor, anotaciones
#%%
def CatColorHistogram(img, num_bins, min_val=None, max_val=None):

    assert len(img.shape) == 3, 'img must be a color 2D image'

    img = img_as_float(img)
    _, _, n_channels = img.shape

    assert isinstance(num_bins, (int, tuple, list, np.array)),'num_bins must be int or array like'

    if isinstance(num_bins, int):
        num_bins = np.array([num_bins]*n_channels)
    else:
        num_bins = np.array(num_bins)

    assert len(num_bins) == n_channels,'num_bins length and number of channels differ'
 
    if min_val is None:
        min_val = np.min(img, (0,1))
    else:
        assert isinstance(min_val, (int, tuple, list, np.array)),'min_val must be int or array like'
        if isinstance(min_val, int):
            min_val = np.array([min_val]*n_channels)
        else:
            min_val = np.array(min_val)

    assert len(min_val) == n_channels,'min_val length and number of channels differ'
    
    min_val = min_val.reshape((1, 1, -1))

    if max_val is None:
        max_val = np.max(img, (0,1))
    else:
        assert isinstance(max_val, (int, tuple, list, np.array)),'max_val must be int or array like'
        if isinstance(max_val, int):
            max_val = np.array([max_val]*n_channels)
        else:
            max_val = np.array(max_val)

    assert len(max_val) == n_channels,'max_val length and number of channels differ'
    max_val = max_val.reshape((1, 1, -1)) + 1e-5
    concat_hist = np.zeros(np.sum(num_bins), dtype=np.int)

    img = (img - min_val) / (max_val - min_val)
    sum_value = 0

    for c in range(n_channels):
        idx_matrix = np.floor(img[...,c]*num_bins[c]).astype('int')
        idx_matrix = idx_matrix.flatten() + sum_value
        sum_value += num_bins[c]
        
        for p in range(len(idx_matrix)):
            concat_hist[idx_matrix[p]] += 1
    
    return concat_hist/np.sum(concat_hist)

