import pickle
import os

def pickle_dump(X,path,filename,):
    pickle_out=open(os.path.join(path,filename),'wb')    #or alternatively we can also use path+'/'+'X.pickle'
    pickle.dump(X,pickle_out)
    pickle_out.close()
    
    
def pickle_read(path,filename):
    pickle_in=open(os.path.join(path,filename),'rb')    #or alternatively we can also use path+'/'+'X.pickle'
    X=pickle.load(pickle_in)
    return X
    pickle_in.close()