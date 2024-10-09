<!--

author:   Tatiana Woller, Benjamin Pavie
email:    training@vib.de
version:  1.0.0
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

@orcid: [@0](@1)<!--class="orcid-logo-for-author-list"-->

# Chapter 4 - BAND, BioImage Analysis (non-Napari)

> [!TIP]
> DISCLAIMER
> 
> It takes a bit of time the first time after login to start the software in general, so be patient
> 

## QuPath

#### Start QuPath
Start it via the menu `Applications › Bioimage analysis › QuPath 0.5.0 `

#### Create a new Project
`File › Project... › Create project`

Store it in `/dodrio/scractch/projects/2024_300/USERNAME/qupath_project`

#### Drag an drop the project folder into qupath
e.g., located in `/dodrio/scractch/projects/2024_300/USERNAME/qupath_project`

#### Add a image into the project
Image are located in `/dodrio/scratch/projects/2024_300/training/qupath/`
![Import image](/images/napari/qupath_00_import.png
 'Import image')

#### Create a new class tissue
![Create new class](/images/napari/qupath_01_create_class.png
 'Create new class')

#### Create a new pixel classififer to detect the tissue
![Tissue detection](/images/napari/qupath_02_parameters_tissue_detection.png
 'Tissue detection')

#### Positive cell detection
![Positive cell detection](/images/napari/qupath_03_parameters_segmentation.png
 'Positive cell detection')

> [!TIP]
> Alternativelly, you can start it via the terminal, then locad manually the module and start QuaPth
> - Load the module
> ```bash
> module purge
> module load QuPath/0.5.0-GCCcore-12.3.0-Java-17
> ```
> - Start QuPath
> ```bash
> QuPath
> ```

> [!TIP]
> Copy paste from outside of `Bioimage ANalysis Desktop` to inside it
> 
> ![Copy/Paste](/images/napari/qupath_00_copy_paste_module.png
 'copy/paste')
 

## CellPose

#### Start
Start it via the menu `Applications › Bioimage analysis › CellPose 2.2.2 CUDA`

#### Open and process a 2D  image
Drag and Drop the tif image located at `/dodrio/scratch/projects/2024_300/training/cellpose/2d/hdab_fat_cells_2d.tif` in cellpose

![CellPose 2D](/images/napari/cellpose_2d.png)

#### Open and process a 3D  image
Drag and Drop the tif image located at `/dodrio/scratch/projects/2024_300/training/cellpose/3d/3d.tif` in cellpose

![CellPose 3D](/images/napari/cellpose_3d.png)

> [!WARNING]
> As you may have noticed, on a small screen, since cellpose version 2.2 is not resizable with a scrollbar, it is sometimes not possible to view the scrollbar to change the Z position.
> 
> Also, the first time your run cellpose with a model, this one will be downloaded and stored into your personal storage (`/dodrio/scratch/users/vscxxxxx/.cellpose/models/`)(when you see `Downloading: "https://www.cellpose.org/models/cyto2torch_0" to /dodrio/scratch/users/vsc33625/.cellpose/models/cyto2torch_0` in the terminal)

#### Batch processing
-  View the parameters
```batch
python -m cellpose --help
usage: __main__.py [-h] [--version] [--verbose] [--use_gpu] [--gpu_device GPU_DEVICE] [--check_mkl] [--dir DIR] [--image_path IMAGE_PATH]
                   [--look_one_level_down] [--img_filter IMG_FILTER] [--channel_axis CHANNEL_AXIS] [--z_axis Z_AXIS] [--chan CHAN] [--chan2 CHAN2]
                   [--invert] [--all_channels] [--pretrained_model PRETRAINED_MODEL] [--add_model ADD_MODEL] [--unet] [--nclasses NCLASSES]
                   [--no_resample] [--net_avg] [--no_interp] [--no_norm] [--do_3D] [--diameter DIAMETER] [--stitch_threshold STITCH_THRESHOLD]
                   [--min_size MIN_SIZE] [--fast_mode] [--flow_threshold FLOW_THRESHOLD] [--cellprob_threshold CELLPROB_THRESHOLD]
                   [--anisotropy ANISOTROPY] [--exclude_on_edges] [--save_png] [--save_tif] [--no_npy] [--savedir SAVEDIR] [--dir_above]
                   [--in_folders] [--save_flows] [--save_outlines] [--save_rois] [--save_ncolor] [--save_txt] [--train] [--train_size]
                   [--test_dir TEST_DIR] [--mask_filter MASK_FILTER] [--diam_mean DIAM_MEAN] [--learning_rate LEARNING_RATE]
                   [--weight_decay WEIGHT_DECAY] [--n_epochs N_EPOCHS] [--batch_size BATCH_SIZE] [--min_train_masks MIN_TRAIN_MASKS]
                   [--residual_on RESIDUAL_ON] [--style_on STYLE_ON] [--concatenation CONCATENATION] [--save_every SAVE_EVERY] [--save_each]

Cellpose Command Line Parameters

options:
  -h, --help            show this help message and exit
  --version             show cellpose version info
  --verbose             show information about running and settings and save to log

Hardware Arguments:
  --use_gpu             use gpu if torch with cuda installed
  --gpu_device GPU_DEVICE
                        which gpu device to use, use an integer for torch, or mps for M1
  --check_mkl           check if mkl working

Input Image Arguments:
  --dir DIR             folder containing data to run or train on.
  --image_path IMAGE_PATH
                        if given and --dir not given, run on single image instead of folder (cannot train with this option)
  --look_one_level_down
                        run processing on all subdirectories of current folder
  --img_filter IMG_FILTER
                        end string for images to run on
  --channel_axis CHANNEL_AXIS
                        axis of image which corresponds to image channels
  --z_axis Z_AXIS       axis of image which corresponds to Z dimension
  --chan CHAN           channel to segment; 0: GRAY, 1: RED, 2: GREEN, 3: BLUE. Default: 0
  --chan2 CHAN2         nuclear channel (if cyto, optional); 0: NONE, 1: RED, 2: GREEN, 3: BLUE. Default: 0
  --invert              invert grayscale channel
  --all_channels        use all channels in image if using own model and images with special channels

Model Arguments:
  --pretrained_model PRETRAINED_MODEL
                        model to use for running or starting training
  --add_model ADD_MODEL
                        model path to copy model to hidden .cellpose folder for using in GUI/CLI
  --unet                run standard unet instead of cellpose flow output
  --nclasses NCLASSES   if running unet, choose 2 or 3; cellpose always uses 3

Algorithm Arguments:
  --no_resample         disable dynamics on full image (makes algorithm faster for images with large diameters)
  --net_avg             run 4 networks instead of 1 and average results
  --no_interp           do not interpolate when running dynamics (was default)
  --no_norm             do not normalize images (normalize=False)
  --do_3D               process images as 3D stacks of images (nplanes x nchan x Ly x Lx
  --diameter DIAMETER   cell diameter, if 0 will use the diameter of the training labels used in the model, or with built-in model will estimate
                        diameter for each image
  --stitch_threshold STITCH_THRESHOLD
                        compute masks in 2D then stitch together masks with IoU>0.9 across planes
  --min_size MIN_SIZE   minimum number of pixels per mask, can turn off with -1
  --fast_mode           now equivalent to --no_resample; make code run faster by turning off resampling
  --flow_threshold FLOW_THRESHOLD
                        flow error threshold, 0 turns off this optional QC step. Default: 0.4
  --cellprob_threshold CELLPROB_THRESHOLD
                        cellprob threshold, default is 0, decrease to find more and larger masks
  --anisotropy ANISOTROPY
                        anisotropy of volume in 3D
  --exclude_on_edges    discard masks which touch edges of image

Output Arguments:
  --save_png            save masks as png and outlines as text file for ImageJ
  --save_tif            save masks as tif and outlines as text file for ImageJ
  --no_npy              suppress saving of npy
  --savedir SAVEDIR     folder to which segmentation results will be saved (defaults to input image directory)
  --dir_above           save output folders adjacent to image folder instead of inside it (off by default)
  --in_folders          flag to save output in folders (off by default)
  --save_flows          whether or not to save RGB images of flows when masks are saved (disabled by default)
  --save_outlines       whether or not to save RGB outline images when masks are saved (disabled by default)
  --save_rois           whether or not to save ImageJ compatible ROI archive (disabled by default)
  --save_ncolor         whether or not to save minimal "n-color" masks (disabled by default
  --save_txt            flag to enable txt outlines for ImageJ (disabled by default)

Training Arguments:
  --train               train network using images in dir
  --train_size          train size network at end of training
  --test_dir TEST_DIR   folder containing test data (optional)
  --mask_filter MASK_FILTER
                        end string for masks to run on. use "_seg.npy" for manual annotations from the GUI. Default: _masks
  --diam_mean DIAM_MEAN
                        mean diameter to resize cells to during training -- if starting from pretrained models it cannot be changed from 30.0
  --learning_rate LEARNING_RATE
                        learning rate. Default: 0.2
  --weight_decay WEIGHT_DECAY
                        weight decay. Default: 1e-05
  --n_epochs N_EPOCHS   number of epochs. Default: 500
  --batch_size BATCH_SIZE
                        batch size. Default: 8
  --min_train_masks MIN_TRAIN_MASKS
                        minimum number of masks a training image must have to be used. Default: 5
  --residual_on RESIDUAL_ON
                        use residual connections
  --style_on STYLE_ON   use style vector
  --concatenation CONCATENATION
                        concatenate downsampled layers with upsampled layers (off by default which means they are added)
  --save_every SAVE_EVERY
                        number of epochs to skip between saves. Default: 100
  --save_each           save the model under a different filename per --save_every epoch for later comparsion
```

#### Run cellpose to process all the images in a folder using similar parameters as the one set using the GUI

- Start the terminal : `Applications › Terminal Emulator`

- FIgure out where you want to store the result. You will have to modify the command below the part (`--savedir /your/personal/storage/`)

- Enter the following command :

```batch
[vsc33625@gpu512 ~]$ python -m cellpose --dir /path/to/personal/storage/3d/ --use_gpu --pretrained_model cyto2 --chan 2 --chan2 1 --do_3D --diameter 80 --flow_threshold 0.1 --cellprob_threshold -5 --save_tif --savedir /your/personal/storage/
>>>> !NEW LOGGING SETUP! To see cellpose progress, set --verbose
No --verbose => no progress or info printed
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 25.3M/25.3M [00:03<00:00, 7.65MB/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 25.3M/25.3M [00:04<00:00, 5.46MB/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 25.3M/25.3M [00:06<00:00, 4.39MB/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 26/26 [00:00<00:00, 302.87it/s]
```
This will save the result into the input directory.

> [!WARNING]
> As you may have noticed, on a small screen, since cellpose version 2.2 is not resizable with a scrollbar, it is sometimes not possible to view the scrollbar to change the Z position.


> [!TIP]
> Alternativelly, you can start it via the terminal `Applications › Terminal Emulator`
, then locad manually the module and start CellPose
> - Load the module
> ```bash
> module purge
> module load Cellpose/2.2.2-foss-2022a-CUDA-11.7.0
> ```
> - Start CellPose
> ```bash
> cellpose
> ```


[previous chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter03.md) | [next chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter05.md)
