#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_core.ipynb (unless otherwise specified).

__all__ = ['stats']

#Cell
def stats(x):
    "Returns `mean` and `std` of a tensor"
    return (x.mean(),x.std())