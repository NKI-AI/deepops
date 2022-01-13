Cosmos cluster management
===

GPU infrastructure and automation tools

## Overview

The DeepOps project encapsulates best practices in the deployment of GPU server clusters and sharing single powerful nodes. DeepOps can also be adapted or used in a modular fashion to match site-specific cluster needs. For example:

* An on-prem data center of NVIDIA DGX servers where DeepOps provides end-to-end capabilities to set up the entire cluster management stack
* An existing cluster that needs a resource manager / batch scheduler, where DeepOps is used to install Slurm, Kubernetes, or a hybrid of both
* A single machine where no scheduler is desired, only NVIDIA drivers, Docker, and the NVIDIA Container Runtime


## Getting Started

For detailed help or guidance, read through our [Getting Started Guide](docs/) or pick one of the deployment options documented below.

### Supported Ansible versions

DeepOps supports using Ansible 2.9.x.
Ansible 2.10.x and newer are not currently supported.

### Supported distributions

DeepOps currently supports the following Linux distributions:

* Ubuntu 18.04 LTS, 20.04 LTS

### Slurm

Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters.

Consult the [DeepOps Slurm Deployment Guide](docs/slurm-cluster/) for instructions on building a GPU-enabled Slurm cluster using DeepOps.

For more information on Slurm in general, refer to the [official Slurm docs](https://slurm.schedmd.com/overview.html).


## Updating DeepOps

To update from a previous version of DeepOps to a newer release, please consult the [DeepOps Update Guide](docs/deepops/update-deepops.md).

## Copyright and License

This project is released under the [BSD 3-clause license](https://github.com/NVIDIA/deepops/blob/master/LICENSE).

## Issues

NVIDIA DGX customers should file an NVES ticket via [NVIDIA Enterprise Services](https://nvid.nvidia.com/enterpriselogin/).

Otherwise, bugs and feature requests can be made by [filing a GitHub Issue](https://github.com/NVIDIA/deepops/issues/new).

## Contributing

To contribute, please issue a [signed](https://raw.githubusercontent.com/NVIDIA/deepops/master/CONTRIBUTING.md) [pull request](https://help.github.com/articles/using-pull-requests/) against the master branch from a local fork. See the [contribution document](https://raw.githubusercontent.com/NVIDIA/deepops/master/CONTRIBUTING.md) for more information.
