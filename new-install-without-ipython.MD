# 1. Install pyglrm wrapper library

```bash
pip install git+https://github.com/rrmina/pyglrm --user
```

# 2. Install Julia 1.10.2

### Download and Extract Julia
```bash
wget https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-x86_64.tar.gz
tar zxvf julia-1.10.2-linux-x86_64.tar.gz
rm -rf julia-1.10.2-linux-x86_64.tar.gz
mkdir $HOME/.julia
mv julia-1.10.2 $HOME/.julia
```

### Open your favorite editor and add julia path

```bash
nano ~/.bashrc
```

### Add these line to the end of file

```text
export PATH="$HOME/.julia/julia-1.10.2/bin:$PATH"
```

### Reload your bash

```bash
source ~/.bashrc
```

# 3. Install the necessary packages in Julia

### Open Julia
```bash
julia
```

### Inside Julia, run these lines
```julia
import Pkg
Pkg.add("PyCall")
Pkg.add("LowRankModels")
exit()
```

# 4. Test Installation

### Run this as a helloworld python script

```python
import numpy as np
from pyglrm import *
    
A = np.array([[1, 2, 3, 4], [2, 4, 6, 8], [4, 5, 6, 7]])

g = glrm(n_components=2) #create a class for GLRM (Here it does PCA)
g.set_training_data(inputs=A)
g.fit()
a_new = np.array([6, 7, 8, 9]) #initialize a new row to be tested
x = g.transform(inputs=a_new) #get the latent representation of a_new
```

via `python-jl`

```bash
python-jl helloworld.py
```
