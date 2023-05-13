# mnist-classifier

Simple MNIST classifier example using PyTorch Lightning.

## Installation

[Install Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if you haven't already.

Create a Conda environment and install dependencies. This MNIST example uses:

- [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/mnist-hello-world.html#Introduction-to-Pytorch-Lightning) for constructing data module and model that can work across machines and utilize accelerator devices (GPUs/TPUs) if available.
- [Hydra](https://hydra.cc) config for cleanly specifying config

### Using Conda (recommended)

```bash
conda env create --file environment.yml
```

Before running any commands below, activate the environment:

```bash
conda activate mnist
```

### Using pip (for demo completeness)

Pip-based installation is not recommended as it provides less control on the dependencies, can be less optimal, and some packages are also only released through Conda. However a `requirements.txt` file is provided here for demo of a pip setup.

```bash
pip install -r requirements.txt
```

## Usage

Inspect/modify the Hydra config at `config.yaml`. Then run:

```bash
# train
python mnist/train.py

# to change configs
python mnist/train.py datamodule.batch_size=64 model.hidden_size=128

# resume training from last checkpoint
python mnist/train.py resume=true
```

This run training with validation at epoch-end, and test when training is done. Metrics will be logged from torchmetrics.

### Hyperparameter Search

By using config-based approach, any variant to the run can be specified as parameter overrides to Hydra configs - hence we can tune hyperparameters without any code changes.

The entrypoint `train.py` returns a float to be used for optimization; the logged metrics in trainer can be accessed via `trainer.callback_metrics`, and the config `cfg.metric` specifies which field.

Hydra has an [Optuna sweeper plugin](https://hydra.cc/docs/plugins/optuna_sweeper/). To run hyperparameter tuning, simply specify the parameter override and search space/details in `config/optuna/`, and run the folllowing:

```bash
# hyperparameter search using Optuna + Hydra. Configure in config/optuna.yaml
# view Optuna sweeper config
python mnist/train.py hydra/sweeper=optuna +optuna=tune -c hydra -p hydra.sweeper
# run Optuna sweeper using optuna/tune.yaml to search over tune and other hyperparams
python mnist/train.py hydra/sweeper=optuna +optuna=tune --multirun
```

### dstack usage

For [dstack](https://docs.dstack.ai) usage, including interactive development, see workflows defined in `.dstack/workflows/*.yaml`.

First, start dstack hub:

```bash
# setup dstack
pip install -U dstack
# start dstack hub
dstack start
```

Then in a new shell, init dstack project and run workflow:

```bash
# initialize project
dstack init
# run training workflow: pip-train
dstack run pip-train
# or run hyperparameter search workflow: pip-tune
dstack run pip-tune
```
