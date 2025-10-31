Title: An introduction to write KernelCI configuration settings for CIP SLTS Kernel project #01
Date: 2025-10-28
Category: kernelci
Tags: kernelci, kernel
Status: draft

[日本語版](https://www.cybertrust.co.jp/blog/linux-learning/kernelci-configuration-settings01.html)

Hello everyone,

My name is Arisu Tachibana.  
I’m the current Gentoo Kernel team leader, creator of KernelCI kci-dev and KernelCI Infra WG member.  
Today I would like to talk about KernelCI configuration and our integration with CIP platforms.  

KernelCI is the project that is used for testing Kernel tree, mostly upstream and development.  

CIP is the project creating SLTS (super long term support kernel), a kernel that is tested using KernelCI.  

For details on the KernelCI project, please check this.  
[https://docs.kernelci.org/about/](https://docs.kernelci.org/about/)  
For details on the CIP project, please check this.  
[https://www.cip-project.org/](https://www.cip-project.org/)  
CIP uses KernelCI for the Linux Kernel.  
[https://www.cip-project.org/about/linux-kernel-core-packages](https://www.cip-project.org/about/linux-kernel-core-packages)  

For adding new boards we should have a lava lab connected with KernelCI,  
my suggestion is to use lava-docker for simplify deploy of a lava laboratory  
([https://github.com/BayLibre/lava-docker](https://github.com/BayLibre/lava-docker))

How to deploy lava-docker will probably be explained in the future, depending on this series sustainability.

Let’s say that you have deployed a lava-docker and you have few devices connected to lava.
You will get a page similar to the one below ([https://lava.ciplatform.org/scheduler/device_types](https://lava.ciplatform.org/scheduler/device_types))

![kernelci_blog01_01]({static}/images/kernelci_blog01_01.png)  

Let’s say that we want to connect zynqmp-zcu102 to KernelCI
We will go to the platforms.yaml file to add the platform information of the platform we want to add

```yaml
platforms:
# arm64 platforms
  zynqmp-zcu102:
    <<: *arm64-device
    mach: zynqmp
    dtb: dtbs/xilinx/zynqmp-zcu102-rev1.0.dtb
    compatible: ['xlnx,zynqmp-zcu102-rev1.0', 'xlnx,zynqmp-zcu102', 'xlnx,zynqmp']
```

dtbs information can be get from the [following page](https://web.git.kernel.org/pub/scm/linux/kernel/git/cip/linux-cip.git/tree/arch/arm64/boot/dts/xilinx?h=linux-6.12.y-cip).

![kernelci_blog01_02]({static}/images/kernelci_blog01_02.png)    

Compatible information can be got from the tools/extract_compatible.py tool
```sh
$ git clone https://github.com/kernelci/kernelci-pipeline.git
$ cd kernelci-pipeline
$ python tools/extract_compatible.py config/platforms-cip.yaml
zynqmp-zcu102:
  compatible: ['xlnx,zynqmp-zcu102-rev1.0', 'xlnx,zynqmp-zcu102', 'xlnx,zynqmp']
```
After we added the platform to KernelCI we can start testing if is working.
For testing the board we should add a simple scheduler, in the CIP case to the file [scheduler-cip.yaml](https://github.com/kernelci/kernelci-pipeline/blob/main/config/scheduler-cip.yaml).

```yaml
scheduler:
  - job: job-gcc-12-arm64-cip
    event:
      <<: *kbuild-gcc-12-arm64-node-event
      name: kbuild-gcc-12-arm64-cip
    runtime:
      type: lava
      name: lava-cip
    platforms:
      - zynqmp-zcu102

  - job: kbuild-gcc-12-arm64-cip
    <<: *build-k8s-all
```
Note:
<<: are part of the [yaml inheritance](https://medium.com/@taha7900/yaml-inheritance-5bb961eb0aac)

The scheduler need to start a kbuild event and after a job event.
The kbuild event will build the kernel with the configurations specified in the job and push the files to the KernelCI fileserver.
The job will perform the platform testing.

The following is the kbuild event creating the kernel image and dts binary.

```yaml
  kbuild-gcc-12-arm64-cip:
    <<: *kbuild-gcc-12-arm64-job
    params:
      <<: *kbuild-gcc-12-arm64-params
      defconfig:
        - defconfig
      fragments:
        - 'CONFIG_ARCH_R8A774A1=y'
        - 'CONFIG_ARCH_ZYNQMP=y'
        - 'kselftest'
        - 'lab-setup'
        - 'cip://6.12.y-cip/arm64/cip_merged_defconfig'
    rules:
      tree:
        - 'cip'
```

Then we have the job event starting the boot test of the platform selected by the scheduler.
```yaml
job-gcc-12-arm64-cip: *baseline-job
```
This will start a job in lava, like the [following example](https://lava.ciplatform.org/scheduler/job/1301506)  

![kernelci_blog01_03]({static}/images/kernelci_blog01_03.png)      

In the next chapter we will execute a simple job example and talk about KernelCI configuration inheritance.
