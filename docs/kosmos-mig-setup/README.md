# MIG setup
The automatic deployement with ansible is not working for now, somehow it seems
to skip `check for NVIDIA MIG parted` in the nvidia-mig role.

Below we describe the steps taken to get a working MIG configuration without the automatic deployment.

### Manual setup
* Deploy slurm-cluster as normal 
* Install mig-parted manually 
* Adjust config and hooks in /etc/nvidia-mig-manager
* The hooks contain services that should be stopped and started before mig changes (this includes any monitoring used by grafana)
* Apply a mig-parted configuration (the kosmos configuration `kosmos-config-a100-80` in /etc/nvidia-mig-manager/config.yml)
* Verify that it has succeeded (with `nvidia-mig-parted export`)
* Use tool to create appropriate `gres.conf` and `allowed_devices` file
* Copy them to the `/etc/slurm` directory _only_ on the MIG enabled node
* Make specific gres options for the different chosen gpu memory profiles

For the service -- reboot persistent:
* select the correct config in `/etc/systemd/system/nvidia-mig-manager/override.conf`
* 

### TODO
* make batch and interactive only -- with a job submission script 
  * ^ such that only have interactive on the debug gpus of 10 gb and the rest only batch