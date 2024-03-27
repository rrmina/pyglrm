# Install pyenv
```bash
curl https://pyenv.run | bash
```

# Add to ~/.bashrc
```text
...
...
... endline

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

# Then rerun your bash
```bash
source ~/.bashrc
```

# Install gcc compiler and other build dependencies
```bash
sudo apt-get update
sudo apt-get install zlib1g zlib1g-dev
sudo apt-get install lzma
sudo apt-get install liblzma-dev
sudo apt-get install libbz2-dev

sudo apt update
sudo apt install \
    build-essential \
    curl \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    llvm \
    make \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev
```

# Build python with shared symbolic links - this will enable ipython of pyglrm
```bash
PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.12.2
```

# Dynamic Link
```bash
ldd ~/.pyenv/versions/3.12.2/bin/python3.12 | grep libpython
```

# Install Julia
```bash
wget https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-x86_64.tar.gz
tar zxvf julia-1.10.2-linux-x86_64.tar.gz
```

# Add Julia to PATH
# Add the following export line to ~/.bashrc
```text
...
...
... endline 

export PATH="$PATH:**julia-1.10.2-INSTALL-PATH**/bin"
```

### example
```text
...
...
... endline 

export PATH="$PATH:/home/rusty/julia-1.10.2/bin"
```


# Then rerun your bash
```bash
source ~/.bashrc
```

# Run julia!
```bash
julia
```

# Inside julia, execute
```julia
import Pkg
Pkg.add("LowRankModels")
Pkg.add("PyCall")
exit()
```

# Install Python Dependencies
```bash
pip install numpy
pip install pandas
python3 -m pip install --user 'https://github.com/JuliaPy/pyjulia/archive/master.zip#egg=julia'
```

# Finally Install pyglrm
pip install git+https://github.com/rrmina/pyglrm --user


# Done!!!

