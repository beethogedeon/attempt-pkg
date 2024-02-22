# Python Package Template

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Last commit](https://img.shields.io/github/last-commit/iSheero-AI/python-package-template.svg?style=flat)](https://github.com/iSheero-AI/python-package-template/commits)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/iSheero-AI/python-package-template)](https://github.com/iSheero-AI/python-package-template/commits)
[![Github Stars](https://img.shields.io/github/stars/iSheero-AI/python-package-template?style=flat&logo=github)](https://github.com/iSheero-AI/python-package-template/stargazers)
[![Github Forks](https://img.shields.io/github/forks/iSheero-AI/python-package-template?style=flat&logo=github)](https://github.com/iSheero-AI/python-package-template/network/members)
[![Github Watchers](https://img.shields.io/github/watchers/iSheero-AI/python-package-template?style=flat&logo=github)](https://github.com/iSheero-AI/python-package-template)
[![GitHub contributors](https://img.shields.io/github/contributors/iSheero-AI/python-package-template)](https://github.com/iSheero-AI/python-package-template/graphs/contributors)


## Tutorial

### Install `cookiecutter` ([Official Instructions](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter))

At the command line:

```bash
python3 -m pip install --user cookiecutter
```

Or, if you do not have pip:

```bash
easy_install --user cookiecutter
```

Though, `pip` is recommended.

Or, if you are using `conda`, first add `conda-forge` to your channels:

```bash
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, cookiecutter can be installed with:

```bash
conda install cookiecutter
```

#### Alternate installations

**Homebrew (Mac OS X only):**

```bash
brew install cookiecutter
```

**Pipx (Linux, OSX and Windows):**

```bash
pipx install cookiecutter
```

**Debian/Ubuntu:**  

```bash
sudo apt-get install cookiecutter
```

#### Upgrading

First, read [History](https://cookiecutter.readthedocs.io/en/latest/HISTORY.html) in detail. There are a lot of major changes. The big ones are:

Cookiecutter no longer deletes the cloned repo after generating a project.

Cloned repos are saved into `~/.cookiecutters/`.

You can optionally create a `~/.cookiecutterrc` config file.

Upgrade **Cookiecutter** either with `easy_install`:

```bash
easy_install --upgrade cookiecutter
```

Or with pip:

```bash
python3 -m pip install --upgrade cookiecutter
```

### Usage

Then, after you have installed `cookiecutter`, execute the following command in the terminal of your choice:

```bash
cookiecutter gh:iSheero-AI/python-package-template
```

## License

This project is collaborative and open source under the [MIT license](LICENSE). Contributions are super appreciated.
