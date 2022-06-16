# Behave template

Behave is a BBD framework for Python. Checks for hoover (matrix dashboard challenge).
Creates HTML reports with "behave-html-formatter".

# Installation

# create project dir
```
mkdir folder && cd folder
```

# Docker
[install Docker](https://docs.docker.com/engine/install/)
* For docker container access reach to devops

# create ans start virtual env with python3
```
virtualenv --python=python3.9.12 .
source bin/activate
```
# get the code

```
git init
git clone git@github.com:alexissoko/behave_test.git
```

# install requirements

[pip install](https://packaging.python.org/en/latest/tutorials/installing-packages/)
```
pip install -r requirements
```

## Usage (bash cmomands adds date stamp to log report)

```bash

# root folder
behave -f html -o oover_challenge_report_$(date +"%Y-%m-%d_%H-%M-%S").html
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
