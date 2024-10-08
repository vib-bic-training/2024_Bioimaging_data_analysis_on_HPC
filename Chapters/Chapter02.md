
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
# Chapter 2 : Data transfer

## Globus

There some different way to transfer data in and out of the CLuster. But the safest way to transfer big chunks of data is using Globus.
​Globus is a research cyberinfrastructure, developed and operated as a not-for-profit service by the University of Chicago.
Globus enables to transfer, share and back-up data regardless of its size and its location 
(i.e. from a supercomputer, drive, laptop, cloud and machines such as a microscope).
In addition, several repositories such EMPIAR or Bioimage archive are using or implementing globus for data deposition/transfer
Globus can execute through a webinterface or through commandline, with/without human interaction.
There is a general session and one session approaching some specifics for Bioimaging.

### Globus setup

#### Authentification 

**$\textcolor{red}{\textsf{Warning}}$** : via the web interface, you can only download one file at a time, see [VSC & globus](https://docs.vscentrum.be/en/latest/globus/using_globus_via_web.html)

1. Browse to the [Globus](https://www.globus.org/) website.
2. Go to Log in (right upper corner)
3. Select your organisation e.g. KU Leuven association/ UGent/ UAntwerp/VIB and click on Continue
4. Follow KU Leuven login procedure via the KU Leuven Authenticator e.g. Scan QR
5. Accept Information to be Provided to Service (always or one time only) and click on Accept
6. Globus App File Manager will be displayed in the browser tab.

#### Installation globus personnal connector 

1. Download globus connector on your computer (if you have a windows pc go to:  https://docs.globus.org/globus-connect-personal/install/windows/ or if you have a mac pc go to: https://docs.globus.org/globus-connect-personal/install/mac/ )
2. Install globus connector on the folder where you have  administrator rights (for KUL in My_Programs or My_Downloads) when the VPN is off.
3. Authentificate 


####  Transferring to active storage (VSC)

<!-- style="color: magenta ;" --> Intro or image to be added

##### From your computer to active storage (VSC)

1. After authentification,  Globus App File Manager will be displayed in the browser tab.
2. Follow Globus file transfer [tutorial](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/globus/managing_and_transferring_files.html#globus-collections-and-endpoints)
3. Use **VSC UGent Tier1 projects** as endpoint and the exact name of the project is "2024_300"

![image](https://user-images.githubusercontent.com/1775952/213488568-e32e144b-d017-4996-85c8-aa82b1266340.png)
  <img width="1216" alt="image" src="https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/f2e2734d-400f-4f23-8bfc-bf907071351d">


 You may authorize the access the first time you login:
 
![image](https://user-images.githubusercontent.com/1775952/213488674-06a2dc3c-664a-409a-bef7-acbbbef2dd43.png)
![image](https://user-images.githubusercontent.com/1775952/213488742-1326bace-f6cb-4f63-9de2-2dcb06d4ae73.png)
![image](https://user-images.githubusercontent.com/1775952/213488873-53e05bd1-5cba-48e8-98f4-9eb2cf81fd74.png)

4. Guidelines for where to store your data are explained [here](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/where_can_i_store_what_kind_of_data.html).

5. You can store data at different places, for example:
- low memory storage backed-up (<3 GB) /dodrio/scratch/users/$VSC_NUMBER/Desktop (= $VSC_SCRATCH/Desktop)
- low memory storage backed-up (<3 GB) /dodrio/scratch/users/$VSC_NUMBER/Ondemand (= $VSC_SCRATCH/Ondemand)
- your own data folder from your institution (=$VSC_DATA)
- active storage that is not backed-up:  /dodrio/scratch/project/starting_2024_300/username (= $VSC_SCRATCH_PROJECTS_BASE/2024_300/username)
- backed-up data: /vsc/home/t1_col_2024_01 (Tier 1 data)

![image](https://user-images.githubusercontent.com/1775952/213489574-493782a0-724e-4c2c-9d44-97b6e20d3f62.png)
<img width="1215" alt="image" src="https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/00f6a18e-d8b8-482a-8fbd-a4c860a77c42">

These folders are accessible via the File Manager in the Bioimage ANalysis Desktop:

![image](https://user-images.githubusercontent.com/1775952/213487170-89eafc68-9b07-42c1-9cc8-1be64b5e1660.png)

6. Checking your disk usage is explained here: https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/managing_disk_usage.html

7. Other endpoints:
- `VSC KU Leuven tier2 scratch (Tier-2 KUL)`: /scratch/xxx/vscxxxyy
- `VSC UGENT Tier2 filesystem (Tier-2 UGent)`: /scratch/gent
- `KU Leuven L drive (LUNA)`
- `KU Leuven Onedrive`
- `VIB shared files`
- `EMPIAR`
- `BioImage archive`
---------------------------------------------------

## Research data management (RDM)

### ManGO
ManGO is developped by KU Leuven as a middelware on the top of iRODS (an open source data management software). 
ManGO is data agnostic and used in different fields (exact science, life science, humanities) and implemented on VSC, University of Wageningen and National Cancer institute in the Netherlands.
Thanks to ManGO, the metadata can be extracted automatically through workflows, the metadata can be added through schema and archived with ease.  

### DataHub
Solution provided by Elixir and VIB (for more info, contact Datacore)

### GitHub
Code should shared on GitHub (Bic code, Bic training and ...)


[previous chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter01.md) | [next chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter03.md)
