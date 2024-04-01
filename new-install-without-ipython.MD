# Install pyglrm wrapper library

```bash
pip install git+https://github.com/rrmina/pyglrm --user
```

# Install Julia 1.10.2

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

# Install the necessary packages in Julia

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
