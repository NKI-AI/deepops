Kosmos configuration
=============================

This directory provides the kosmos configuration.
The files in this directory will help determine the behavior of the Ansible playbooks and other scripts that DeepOps uses to set up your systems.

For more details on how this works, see [how to configure DeepOps](../docs/deepops/configuration.md).

## MIG
The possible Multiple Instance GPU configurations are listed in [nvidia-mig-config.yml](nvidia-mig-config.yml), our specific setup is called 'kosmos-config-a100-80'.
It is configured to have 6 GPUs with full 80gb memory and 2 GPUs, each split up into 7 instances with 10 gb memory. For details on possible configurations see [NVIDIA's website](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html).