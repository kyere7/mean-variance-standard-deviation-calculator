import numpy as np

def calculate(list):
    if (len(list) !=9):
        raise ValueError("List must contain nine numbers.")
        
    list = np.array(list)
    matrix = list.reshape(3,3)
    #calculate means 
    mean_ax1 = matrix.mean(axis=0).tolist()
    mean_ax2 = matrix.mean(axis=1).tolist()
    mean_flat = np.mean(list).tolist()
    
    #calcuate variance
    var_ax1 = matrix.var(axis=0).tolist()
    var_ax2 = matrix.var(axis=1).tolist()
    var_flat = np.var(list).tolist()

    #calcuate standard deviation
    st_ax1 = matrix.std(axis=0).tolist()
    st_ax2 = matrix.std(axis=1).tolist()
    st_flat = np.std(list).tolist()

    #calculate max
    maxi_ax1 = matrix.max(axis=0).tolist()
    maxi_ax2 = matrix.max(axis=1).tolist()
    maxi_flat = np.max(list).tolist()

    #calculate min
    mini_ax1 = matrix.min(axis=0).tolist()
    mini_ax2 = matrix.min(axis=1).tolist()
    mini_flat = np.min(list).tolist()

    #calculate sum
    su_ax1 = matrix.sum(axis=0).tolist()
    su_ax2 = matrix.sum(axis=1).tolist()
    su_flat = np.sum(list).tolist()

    calculations = {
    "mean": [mean_ax1,mean_ax2, mean_flat],
    "variance": [var_ax1,var_ax2, var_flat],
    "standard deviation": [st_ax1,st_ax2, st_flat],
    "max": [maxi_ax1,maxi_ax2, maxi_flat],
    "min": [mini_ax1,mini_ax2, mini_flat],
    "sum": [su_ax1,su_ax2, su_flat]
  }
  
    return calculations
