#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_core.ipynb (unless otherwise specified).

__all__ = ['stats', 'log_softmax', 'plotdist']

#Cell
def stats(x):
    "Returns `mean` and `std` of a tensor"
    return x.mean(),x.std()

#Cell
def log_softmax(x):

    return x - x.exp().sum(-1).log().unsqueeze(-1)

#Cell
def plotdist(x):
    "Plot distribution `x`"
    fig = plt.figure(figsize=(4,3))
    m,s = x.mean(), x.std()
    n,_,_ = plt.hist(x.reshape(-1),bins=100);
    l = [i*s for i in (-3,-2,-1,1,2,3)] # three sigmas
    l.append(m) # plus mean
    plt.vlines(l, 0, n.max(), color='white', alpha=0.2)
    ax = plt.title(f'Mean = {round(float(m),3)}; $\sigma$ = {round(float(s),3)}');