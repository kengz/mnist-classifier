# mnist-classifier

Simple MNIST classifier example using PyTorch Lightning.

## Installation

[Install Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if you haven't already.

Create a Conda environment and install dependencies. This MNIST example uses:

- [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/mnist-hello-world.html#Introduction-to-Pytorch-Lightning) for constructing data module and model that can work across machines and utilize accelerator devices (GPUs/TPUs) if available.
- [Hydra](https://hydra.cc) config for cleanly specifying config

```bash
conda create -n mnist python=3.10.4 -y
conda activate mnist
pip install pytorch-lightning pillow torchvision
pip install hydra-core=1.2.0
```

## Usage

Inspect/modify the Hydra config at `config.yaml`. Then run:

```bash
python mnist/train.py
```

This run training with validation at epoch-end, and test when training is done. Metrics will be logged from torchmetrics.

### dstack usage

```bash
conda activate mnist
pip install -U dstack

dstack run download
dstack run train
```
