
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
# Chapter 3 : BAND Napari


## Start BAND:

1. Connect to https://tier1.hpc.ugent.be
2. Go to `My Interactive Sessions `
3. Configure your BAND virtual desktop for the analysis
   1. Cluster : `dodrio gpu_rome_a100`
   2. Time (hours) : `2`
   3. Number of node : `1`
   4. Number of Core : `12 cores (quarter) or 8 cores or 16 cores`
   5. Number of GPU per node : `1`
   6. Project Account: 2024_300
   7. Reservation none 
   8. Select advanced properties and accelerate the whole desktop
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/cfb50903-77b4-4f97-a895-1adb8167d65d)
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/a1b9e0b2-3953-42ee-9f6d-c24ed8f74c19)

The selection of the cluster (using or not using GPU), of the time and the number of cores depends on which software you want to use (i.e. Napari relies on GPU while Fiji and QuPath do not), how big your dataset is and which analysis you want to do. In case of doubt, feel free to contact Benjamin.


## Access to the pre-install software

Most of the pre-installed software are accessible via the Menu `Application › BioImage Analysis › ...
![Menu BioImage Analysis](/images/napari/00_application_bioimage_analysis_menu.png 'Menu BioImage Analysis')

| Name    | Application |
| -------- | ------- |
| napari 4.0.19 devbio empanada  | napari + devbio + empanada    |
| napari 4.0.19 devbio empanada | napari + devbio + empanada already on the assistant interface     |
| napari 4.0.19 n2v    | napari [noise2void](https://juglab.github.io/napari-n2v/)    |

## 1- Napari devbio

A bundle of napari plugins useful for 3D+t image processing and analysis for studying developmental biology, developped by Robert Haase and Co, [more info](https://github.com/haesleinhuepf/devbio-napari)

Start via the menu `Application › napari 4.0.19 devbio empanada assistant`

> [!TIP]
> Alternativelly, you can start it via the terminal, then locad manually the module and start it
> - Load the module
> ```bash
> module purge
> module activate devbio-napari/0.10.1-foss-2022a-CUDA-11.7.0
> ```
> - Start
> ```bash
> napari
> ```

> [!TIP]
> Copy paste from outside of `Bioimage ANalysis Desktop` to inside it
> 
> ![Copy/Paste](/images/napari/03_devbio_copy_paste.png
 'copy/paste')
> 
### Interface
1. Load the demo image : `File › Open Sample › napari builtins › Cells (3D+2Ch)`
![Napari Interface](/images/napari/05_devbio_napari_interface.png
 'Napari Interface')

### Create Manual labels
https://github.com/tatianawoller/Training_prep_290524/blob/main/images/napari/06_devbio_create_label.mp4
![Napari Interface](/images/napari/06_devbio_create_label_02.gif
 'Napari Interface')
<!-- 
### Install Plugins
- List of available plugins : https://www.napari-hub.org/
- **>400 plugins** are currently available

![Napari Plugins](/images/napari/07_devbio_napari_plugin.png
 'Napari Plugins')
-->
### Using Devbio assistant - Nuclei 3d Segmentation

2. Start the Assistant : Tools › Utilities › Assistant
![Napari Plugins](/images/napari/08_devbio_napari_assistant.png
 'Napari Plugins')
2. Select the nuclei layer
5. Remove noise › Gaussian blur 1
![Remove noise](/images/napari/09_devbio_napari_assistant_remove_noise.png
 'Remove noise')
6. Label › Voronoi otsu labeling 9/2
![Voronoi Otsu Labeling](/images/napari/10_devbio_napari_assistant_voronoi_otsu_labeling.png
 'Voronoi Otsu Labeling')
7. Process Label › Closing
![Label Closing](/images/napari/11_devbio_napari_assistant_process_label_closing.png
 'Label Closing')
### Using segment blobs and things - Cell Segmentation using seeded watershed
7. Seeded watershed segmentation : `Plugins › napari-segment-blobs-and-things-with-membranes › seeded watershed`
![Seeded Watershed](/images/napari/12_devbio_napari_segment-blobs-and-things_seeded-watershed.png
 'Seeded watershed')

### Using Devbio assistant - Exclude edge cells
8. Process Label › exclude labels on edge (x/y)
![Exclude labels on edge](/images/napari/13_devbio_napari_assistant_exclude_label_on_edges.png
 'Exclude labels on edge')

### Using Devbio assistant - Pipeline step overview
![Exclude labels on edge](/images/napari/15_devbio_napari_segmentation_result_overview.png
 'Exclude labels on edge')

 ## 2- Napari n2v

N2V is a sef-supervised denoising algorithm allowing removing pixel-independent noise, [more info]([https://juglab.github.io/napari-n2v/)

- Dataset
Dataset are located in : `https://juglab.github.io/napari-n2v/` and a sub-folder `training` will be used to train a denoising model.

- Training
  - Start via the menu `Application › napari 4.0.19 devbio empanada assistant`
  - Drag and drop the images located in training folder into napari. Keep only 2 and rename one to be `training` and the other one to be `validation`
  - Start the plugin `Plugins › napari-n2v › N2V Train`
  - Train a model:
  ![N2V training](/images/napari/01_napari_n2v.png 'N2V Training')

          | Parameters    | Value |
          | -------- | ------- |
          | Train  | training    |
          | Validation | validation  |
          | Axes | XY |
          | N epochs | 20 |
          | N steps | 200 |
          | Batch size | 16 |
          | Patch XY | 64 |

  - click on `Training` and follow the evolution of the loss function along the different epoch

  ![N2V training](/images/napari/01_napari_n2v_b.png 'N2V Training')

  - Save the model: save the model as `Keras` or `Tensorflow` and remember where you save them (name should end with `.zip` for Tensorflow and `.h5` for keras

- Predict :
  - Copy the dataset to denoise to your directory from `/dodrio/scratch/projects/2024_300/training/n2v/` to `/dodrio/scratch/projects/2024_300/YOUR_NAME/dataset/`
  - Close the previous plugin
  - Start the plugin `Plugins › napari-n2v › N2V Predict`
  - Select `From disk`
  - Select `Lazy loading`
  - Choose the path to where the file you want to denoise are located, e.g. `/dodrio/scratch/projects/2024_300/YOUR_NAME/dataset/`
  - Select the model you saved previously
  - Click on Predict
    
    ![N2V training](/images/napari/02_napari_n2v.png 'N2V Training')
 
  At the end, you should see a preview of the dataset denoised:
  
    ![N2V training](/images/napari/03_napari_n2v.png 'N2V Training')

## 3- Napari - Empanada

empanada-napari allow you to run Panoptic segmentation algorithms for 2D and 3D electron microscopy in napari to e.g. segment mitochondria, E.R., see [website](
https://empanada.readthedocs.io/en/latest/tutorials/2d_tutorial.html#d-inference-tutorial)

- Start napari via the menu `Application › napari 4.0.19 devbio empanada assistant`

- Start the plugin `Plugins › empanada-napari › 2D Inference (Parameter Testing)`

- Open the folder `File › Open Folder...` and select the folder containing the images for empanada located at `/dodrio/scratch/projects/2024_300/training/empanada/`

    ![Napari open folder](/images/napari/napari_open_folder.png 'Napari open folder')

    
- Leave the default parameters:

  ![Napari empanada](/images/napari/01_napari_empanada.png 'Napari empanada')

- Click on `Run 2D inference`
> [!Warning]
> It will download the mitonet model in `/dodrio/scratch/users/vscxxxxx/.empanada/MitoNet_v1.pth`, which is around 221MB, so it will take some space on the limted space you have on your personal space.

At the end you should the that the images have been segmented using the mitonet_v1 model
      ![Napari empanada](/images/napari/02_napari_empanada.png 'Napari empanada')




