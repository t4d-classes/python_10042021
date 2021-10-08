

1. Install PyEnv Windows from here: [https://pyenv-win.github.io/pyenv-win/#installation](https://pyenv-win.github.io/pyenv-win/#installation)

1. To display the global Python version:

```pwsh
pyenv global
```

1. To display the local Python version:

```pwsh
pyenv local
```

1. To display a list of Python versions to install:

```pwsh
pyenv install --list
```

1. To display a list of Python versions for a particular version:

```pwsh
pyenv install --list | Select-String -Pattern "^3.8"
```

1. Install Python version `3.8.10`:

```pwsh
pyenv install 3.8.10
```

1. Set global to version `3.8.10`:

```pwsh
pyenv global 3.8.10
```

1. Check Python version:

```pwsh
python --version
```

1. Create a new folder, and change into it:

```pwsh
mkdir some-app

cd some-app
```

1. Install Python version `3.9.6`:

```pwsh
pyenv install 3.9.6
```

1. Set local version to `3.9.6`

```pwsh
```

1. View installed versions:

```pwsh
pyenv versions
```

