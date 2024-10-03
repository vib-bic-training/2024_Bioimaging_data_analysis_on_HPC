<!--

author:   Pavie Benjamin
email:    benjamin.pavie@vib.de
version:  2.0.0
language: en
narrator: UK English Female

icon:     https://vib.be/sites/vib.sites.vib.be/files/logo_VIB_noTagline.svg

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/img/org.css
link:     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css
link:     https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@300&display=swap
link:     https://fonts.googleapis.com/css2?family=Open+Sans&display=swap
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/vib-styles.css

tutor:    VIB
edition:  1st 
workshop_name:     Bioimaging data analysis on HPC
workshop_edition: 1st

@JSONLD
<script run-once>
  let json = @0 

  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.text = JSON.stringify(json);

  document.head.appendChild(script);

  // this is only needed to prevent and output,
  // as long as the result of a script is undefined,
  // it is not shown or rendered within LiaScript
  console.debug("added json to head")
</script>
@end

orcid:    [@0](@1)<!--class="orcid-logo-for-author-list"
-->


## Infrastructure

Check here what are the clusters available in each section of the VSC. You can see the names and some of the resources linked to each of them. This might not make much difference for you now, but is very useful when you wan to optimize your analysis and pipelines.

Sending a job into an appropriate cluster can make the difference in how much time you wait in the "line" and how much memory you will have available for example.

### UGent VSC

If for your training session you are using the [UGent section]((https://docs.vscentrum.be/gent/tier2_hardware.html) or Tier1 of the [Flemish Supercomputing Center](https://www.vscentrum.be/), it's very likely that you will be using the GPU cluster and debug cluster through the. As you can imagine this is not the only cluster you can use, but for trai is good to have an interactive session in order to understand how it is working.

<!-- style="color: #7CA1CC;" --> Each section of the **VSC** has independent managing systems. 

It means that the files and storage systems in place **will vary**. Knowing this details will be important to understand ***how*** and ***where*** to keep , analyze and backup your data.

As you probably already guessed, there is a difference if we are talking about personal use and project wise. Specific projects might request specific resources and will define who can access it.

Overview UGent VSC
-------------
<!-- style="color: magenta" --> VO = virtual organization

| Tier  | Login (vscnumber) | Personal storage space | VO Storage Space |  VO Project space |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Tier 1 | tier1.hpc.ugent.be |yes|yes|yes|
|Tier 2 Ghent | login.hpc.ugent.be |yes|yes|none|

UGent VSC Clusters
-----------------------------------

On top of the filesystem, each clusters will have different computational powers, therefore, depending on your needs, you can choose the one that most suits you.

| Cluster name  | Memory (GiB) | Disk space  |  GPU |
|---|---|---|---|
| swalot | 116 | 1 TB | - |
| skitty | 177 | 1 TB + 240 GB SSD | - |
| victini | 88 | 1 TB + 240 GB SSD | - |
| joltik | 256 | 800 GB SSD | 4 NVIDIA V100 |
| doduo | 250 | 180 GB SSD | - |
| accelgor | 500 | 180 GB SSD | 4 NVIDIA A100 |
| donphan ** | 738 | 1.6 TB NVME | 1 shared NVIDIA Ampere A2 |
| gallade | 940 | 1.5 TB NVME | - |

\** [debugging cluster (Used for debugging and training)](https://docs.hpc.ugent.be/Linux/interactive_debug/)

--------------------------------------------------------------------------

#### UGent TIER 1

| Cluster name  | Memory (GiB) | Disk space (GB) SSD  |  GPU | GPU memory (GiB)|
| --- | --- | --- | --- | --- |
| cpu_rome | 256 | 480 | - | - |
| cpu_rome_512 | 512 | 480 | - | - |
| cpu_milan | 256 | 480 | - | - |
| gpu_rome_a100_40| 256 | 480 | 4 NVIDIA A100  | 40 |
| gpu_rome_a100_80 | 512 | 480 | 4 NVIDIA A100  | 80 |
| debug_rome ** | 256| 100 | 1 NVIDIA Quadro P1000 | 4 |

\** [debugging cluster (Used for debugging and training)](https://docs.hpc.ugent.be/Linux/interactive_debug/)

NB: There are two additional two clusters called `cpu_rome_all` and `gpu_rome_a100`.
- `cpu_rome_all corresponds` to a combination of `cpu_rome` and `cpu_rome_512`.
- `gpu_rome_a100_all` corresponds to a combination of `gpu_rome_a100_40` and `gpu_rome_a100_80`.


Filesystems specifics
---------------------------

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space ** |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, Not the entry point to the system, same as Tier2 | ? | 3GB (fixed) | ❌ |
| $VSC_SCRATCH | Entry point to the system | ? | 3GB (fixed) | ❌ |
| $VSC_DATA | Long-term storage of large data files | ? | Depend of you account(Leuven/Gent, see above) | ❌ |
| $VSC_SCRATCH_PROJECTS_BASE/2024_300/| Temporary fast storage of ‘live’ data for calculations | ? | 20TB | upon request |

<!-- style="color: #7CA1CC;" --> \** Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

> Source : https://docs.vscentrum.be/gent/tier1_hortense.html#system-specific-aspects
> For more information on the different partitions: https://docs.vscentrum.be/en/latest/gent/tier1_hortense.html#general-information

---------------------------------------------

Check the quota
---------------------

`my_dodrio_quota`

```bash
Userquota:
Disk quotas for prj 2534840 (pid 2534840):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /dodrio  1.709G   2.85G      3G       -   24566  1048576 1048576       -

Quota for project gpr_compute_2024_300:
Disk quotas for prj 2641240 (pid 2641240):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /dodrio   15.4T     19T     20T       -  739564  1048576 1048576       -
```

On Tier1, `my_dodrio_quota` give the space available on the `$VSC_SCRATCH` (first result) and on the one on our project (in that case `/dodrio/scratch/projects/2024_300/`)

---------------------------------------------------------


#### UGent TIER 2

 `show_quota` or go to https://account.vscentrum.be for a general overview


Filesystems specifics
---------------------------

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space (*) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, entry point to the system | 51 TB | 3GB (fixed) | ❌ |
| $VSC_DATA | Long-term storage of large data files | 1.8 PB | 25GB (fixed) | 250GB |
| $VSC_SCRATCH | Temporary fast storage of ‘live’ data for calculations | 1.9 PB | 25GB (fixed) | 250GB |
| $VSC\_SCRATCH\_ARCANINE | Temporary very fast storage of ‘live’ data for calculations (recommended for very I/O-intensive jobs) | 70 TB  | (none) | upon request |
(*) Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

> Source : https://docs.vscentrum.be/en/latest/gent/tier2_hardware.html?highlight=VSC_DATA#shared-storage

----------------------------------------------


### KULeuven VSC

If for your training session you are using the [KULeuven section](https://docs.vscentrum.be/leuven/genius_quick_start.html#access-to-the-cluster) of the [Flemish Supercomputing Center](https://www.vscentrum.be/), it's very likely that your group is in a list of people with priorities for a reserved cluster. As you read this you can imagine that there is not only cluster option you can use. Different clusters will have different computational powers, therefore, depending on what you will do you can choose the one that most suits you.

Overview KULeuven-VSC 
-------------

<!-- style="color: magenta" --> To update


| Tier  | Login (vscnumber) | Personal storage space | VO Storage Space |  VO Project space |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Tier 2 Leuven | login.hpc.kuleuven.be | yes | yes | none |

Clusters specifics at KULeuven - VSC
-----------------------------------

#### Tier 2 KUL Genius

| Cluster name | Memory (GiB) | Disk space  | GPU | GPU memory (GiB) |
| --- | --- | --- | --- | --- |
| batch/batch_long | 192 | 200 GB SSD | - | - |
| interactive | 192 | 200 GB SSD | - | - |
| bigmem | 768 | 200 GB SSD | - | - |
| gpu_p100 | 192 | 200 GB SSD | 4 NVIDIA P100 | 16 |
| GPU_v100 | 768 | 200 GB SSD | 8 NVIDIA V100 | 32 |
| AMD | 256 | 200 GB SSD | - | - |

-----------------------------------------------

####  Tier 2 KUL wICE

| Cluster name | Memory (GiB) | Disk space  | GPU | GPU memory (GiB) |
| --- | --- | --- | --- | --- |
| batch/batch_long | 256 | 960 GB SSD | - | - |
| batch\_sapphirerapids **or** batch\_sapphirerapids_long | 256 | 960 GB SSD | - | - |
| bigmem | 256 | 2048 GB SSD | - | - |
| hugemem | 960 | 8000 GB SSD | - | - |
| gpu | 512| 960 GB SSD | 4 NVIDIA A100 SXM4 | 80 |
| gpu_h100 | 768 | 960 GB SSD | 4 NVIDIA H100 | 80 |
| interactive and gpu_a100_debug | 512 | 960 GB SSD | 1 NVIDIA A100 | 80 |


Filesystems specifics
---------------------------

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space (*) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, entry point to the system | ? | 3GB (fixed) | ❌ |
| $VSC_DATA | Long-term storage of large data files | ? | 75GB (fixed) | ❌ |
| $VSC_SCRATCH | Temporary fast storage of **live** data for calculations | ? | 500GB | ? |

<!-- style="color: magenta" --> What do we need the below info? (Bruna - check if there is the same for UGent)

| Variable | Name | 
| ------------- | ------------- |
| $VSC_HOME | /user/leuven/30X/vsc30XYZ | 
| $VSC_DATA | /data/leuven/30X/vsc30XYZ|
| $VSC_SCRATCH **or** $VSC\_SCRATCH\_SITE | /scratch/leuven/30X/vsc30XYZ |
| $VSC\_SCRATCH\_NODE | /local_scratch |

> Source : https://docs.vscentrum.be/en/latest/leuven/tier2_hardware/kuleuven_storage.html?highlight=VSC_DATA#ku-leuven-storage

-----------------------------------------------------------------


Projects and reservation for Tier-2 KU Leuven
-----------------------------------------------

Running calculations on Tier-2 KU Leuven requires credits. New users obtained 2 millions free credits (introduction) that are valid during 6 months.
Credits can be obtained through various type of research projects (through university, FWO, EU level). Subset of Tier-2 KUL can be reserved for research events or training events.

-------------------------------------------------

*****************************************************
## Introduction to HPC

High performance computing (HPC) is a technology that uses clusters of powerful processors, working in parallel, to process massive multi-dimensional datasets (big data) and solve complex problems at extremely high speeds. HPC systems typically perform at speeds more than one million times faster than the fastest commodity desktop, laptop or server systems. [https://www.ibm.com/topics/hpc].

HPC is extremely valuable for fields where deep-learning and machine learning algorithms are daily routine for example.

The European model for HPC consists of three levels of computing capacity:

1. When available at research institutions its called Tier-2.

2. When provided at the level of a region/country because it exceeds the capacity of an institution in terms of needs/costs its called Tier-1.

3. When available at EU level, with **very** large-scale computing infrastructure, its called Tier-0.

**By contrast, Tier-3 corresponds to single computers (your own infrastructure)**


> Flemish super computing centre (VSC)
>
> REF: https://www.vscentrum.be/about
> The Flemish Supercomputing Centre (_Vlaams Supercomputer Center_) is a collaboration between the five universities in Flanders
> - VUB
> - KU Leuven
> - UGent
> - UHasselt
> - UAntwerpen). 
> [replace with the logo of each university for a better visual]
>
>The VSC has developed a differentiated infrastructure (Tier-1 and Tier-2 level) that is available to the academic and business world. 
> Researchers of those universities can get access to Tier-2 infrastructures through their university for free or for a preferential prices.
> In addition, access to Tier-1 infrastructures is allocated through project grants.
> The Tier-1 services encompass :
> - Tier-1 data (active storage and RDM)
> - Tier-1 cloud (virtual machines and etc...)
> - Tier-1 compute (calculations, access through terminal or through graphical user interface through Open On Demand)

## Creating a job

<!-- style="color: magenta ;" --> To be developed

- There is several queues for different kind of jobs (memory, presence or absence gpus, test queues)
- Reservation (fast queue with reservation flag for training)
- Talk about documentation and how to navigate 


### Installed software

#### Easy build modules

From a terminal (or from a Jupyter notebook, add a `!` to use this command)

- See loaded modules
```
ml
module list
```
- See available modules 
```
module avail
```
- Search for a module X
```
module av |& grep -i X
```
- Search for a module X and get details
```
module spider X
```
- Load a module X
```
module load x
```
- Unload a module X
```
module unload x
```
- Swap a module Y to X
```
module swap Y  X
```
- Remove all loaded modules except the cluster one
```
module purge
```
⚠️ Do not load modules built with intel and foss toolchains

🗎 https://docs.vscentrum.be/software/software_stack.html#using-the-module-system

#### How to load module in jupyter notebook
Select the appropriate version of the jupyter notebook and load the easy build module accordingly

![image](../images/Chapter01_jupyter.png)

i.e. 6.4.0 GCC core 11.3.0 IPython 8.5.0 is compatible with foss-2022a or intel 2022a modules (see compatibility table below)

| FOSS  | GCC |  CUDA | OpenMPI | OpenBLAS | FFTW | ScaLAPACK |
| ------| --- | ----- | ------- | -------- | ---- | --------- |
| 2022b | 12.2.0 | 12.0.0 | 4.1.4 | 0.3.21 | 3.3.10 | 2.2.0-fb |
| 2022a | 11.3.0 | 11.7.0 | 4.1.4 | 0.3.20 | 3.3.10 | 2.2.0-fb |
| 2021b | 11.2.0 | - | 4.1.1 | 0.3.18 | 3.3.10 | 2.1.0-fb |
| 2021a | 10.3.0 | - | 4.1.1 | 0.3.15 | 3.3.9 | 2.1.0-fb |
| 2020b | 10.2.0 | - | 4.0.5 | 0.3.12 | 3.3.8 | 2.1.0 |
| 2020a | 9.3.0 | - | 4.0.3 | 0.3.9 | 3.3.8 | 2.1.9 |
| 2019b | 8.3.0 | - | 3.1.4 | 0.3.7 | 3.3.8 | 2.0.2 |

For more information about modules: https://hprc.tamu.edu/kb/Software/GNU-Compiler-Collection/ 

#### Compatibility Python - GCCcore

#### Tier 1

Table for jupyter notebook
 
| IPython version | Python | GCCcore |
| ------------- | ------------- | ------------- |
| 7.25.0-GCCcore-10.3.0 | Python 3.9.5 | GCCcore-10.3.0 |
| 6.4.0-GCCcore-11.2.0 | Python 3.9.6 | GCCcore-11.2.0 |
| 8.5.0-GCCcore-11.3.0 | Python 3.10.4 | GCCcore-11.3.0 |
| 7.0.3 GCCcore 12.2.0 | Python 3.10.8 | GCCcore 12.2.0 |
| 7.0.2 GCCcore 12.3.0 | Python 3.11.3 | GCCcore 12.3.0 |


 How to see what is loaded with the module:
 ``` ml show  IPython/8.5.0-GCCcore-11.3.0 ```

#### Modules for bioimage analysis in python
1. [Napari](https://github.com/napari/napari): Napari/0.4.15-foss-2021b
2. [Cellpose](https://github.com/MouseLand/cellpose): Cellpose/2.2.2-foss-2022a or Cellpose/2.2.2-foss-2022a-CUDA-11.7.0
3. Omnipose:  Omnipose/0.4.4-foss-2022a-CUDA-11.7.0 or  Omnipose/0.4.4-foss-2022a
4. [stardist](https://github.com/stardist/stardist): stardist/0.8.3-foss-2021b-CUDA-11.4.1 or stardist/0.8.3-foss-2021b
5. [AICSImageIO](https://github.com/AllenCellModeling/aicsimageio) : AICSImageIO/4.14.0-foss-2022a
6. [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) : devbio-napari/0.10.1-foss-2022a-CUDA-11.7.0
7. [n2v](https://github.com/juglab/n2v) : n2v/0.3.2-foss-2022a-CUDA-11.7.0
8. Monai: MONAI/1.0.1-foss-2022a
9. Napari-denoiseg:napari-denoiseg/0.0.1-foss-2023a
10. Napari-microsam: micro-sam/1.0.1-foss-2023a
11. Napari empanada:empanada-napari/1.1.0-foss-2023a
12. QuPath: QuPath/0.5.0-GCCcore-12.3.0-Java-17
13. Cellprofiler: CellProfiler/4.2.4-foss-2021a
14. Fiji: Fiji/2.9.0-Java-1.8

#### Module for spatial omics in python
1. [Scanpy](https://github.com/scverse/scanpy): scanpy/1.9.1-foss-2021b
2. Seurat: Seurat/4.3.0-foss-2021b-R-4.1.2
3. Squidpy: Squidpy/1.2.2-foss-2021b
4. [Giotto](https://drieslab.github.io/Giotto/): Giotto-Suite/3.0.1-foss-2022a-R-4.2.1

#### Module for bio-image analysis tools
1. Fiji: Fiji/2.9.0-Java-1.8
2. Cellprofiler: CellProfiler/4.2.4-foss-2021a

#### General libraries 
1. Scikit-learn: scikit-learn/1.1.2-foss-2022a or scikit-learn/1.0.1-foss-2021b
2. Scikit-image: scikit-image/0.19.3-foss-2022a or scikit-image/0.19.1-foss-2021b
3. scipy: SciPy-bundle/2022.05-foss-2022a, SciPy-bundle/2021.10-foss-2021b
4. seaborn: Seaborn/0.11.2-foss-2021b
5. tifftile: Scikit-image/0.19.1-foss-2021b 
6. tensorflow: TensorFlow/2.7.1-foss-2021b-CUDA-11.4.1 or TensorFlow/2.7.1-foss-2021b
7. R : R/4.2.1-foss-2022a or R/4.0.0-foss-2020a
8. R studio: RStudio-Server/1.3.959-foss-2020a-Java-11-R-4.0.0 
9. Jupyter notebook: JupyterLab/3.1.6-GCCcore-11.2.0
10. Matplotlib: matplotlib/3.5.2-foss-2022a or matplotlib/3.4.3-intel-2021b
11. Bioconductor:  R-bundle-Bioconductor/3.14-foss-2021b-R-4.1.2






