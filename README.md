# mnist-classifier

Simple MNIST classifier example using PyTorch Lightning.

## Installation

[Install Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if you haven't already.

Create a Conda environment and install dependencies. This MNIST example uses:

- [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/mnist-hello-world.html#Introduction-to-Pytorch-Lightning) for constructing data module and model that can work across machines and utilize accelerator devices (GPUs/TPUs) if available.
- [Hydra](https://hydra.cc) config for cleanly specifying config

### Using Conda (recommended)

```bash
conda env create --file environment.yml
```

### Using pip (for demo completeness)

Pip-based installation is not recommended as it provides less control on the dependencies, can be less optimal, and some packages are also only released through Conda. However a `requirements.txt` file is provided here for demo of a pip setup.

```bash
pip install -r requirements.txt
```

## Usage

Inspect/modify the Hydra config at `config.yaml`. Then run:

```bash
# train. if previous training exists, it will resume from the last checkpoint.
python mnist/train.py

# to change configs
python mnist/train.py datamodule.batch_size=64 model.hidden_size=128

# start afresh
python mnist/train.py resume=false
```

This run training with validation at epoch-end, and test when training is done. Metrics will be logged from torchmetrics.

### dstack usage

For use with [dstack](https://github.com/dstackai/dstack), [install the CLI](https://docs.dstack.ai/installation/) and [initialize the repo](https://docs.dstack.ai/quickstart/#init-the-repo), then run the workflow defined in `.dstack/workflows.yaml`.

```bash
conda activate mnist

# setup dstack
pip install -U dstack
dstack config

# run workflow
dstack run setup-train
```
