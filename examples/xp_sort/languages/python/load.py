import numpy as np

def load_input(filename):
    
    tabtype = filename.split("/")[4]
    
    tab = np.loadtxt(filename)
    
    if tabtype == 'int':
        tab = tab.astype(int)
        
    return tab
