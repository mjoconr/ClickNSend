<div align="center" style="font-size: 22pt;"> 
  <h1 style="text-align: center;">ClickNSend  </h1>
  <a href="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Badge: Made with Python"/>
  </a>
  <a href="https://img.shields.io/github/stars/bankh/ClickNSend">
    <img src="https://img.shields.io/github/stars/bankh/ClickNSend" alt="GitHub User's stars"/>
  </a>
  <a href="https://img.shields.io/github/forks/bankh/ClickNSend">
    <img src="https://img.shields.io/github/forks/bankh/ClickNSend" alt="GitHub forks"/>
  </a>
  <a href="https://img.shields.io/github/contributors-anon/bankh/ClickNSend">
    <img src="https://img.shields.io/github/contributors-anon/bankh/ClickNSend" alt="GitHub contributors"/>
  </a>
  <a href="https://github.com/bankh/ClickNSend/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>

[Folder Structure](#folder-structure-of-the-repository)📂 | [Installation and Setup](#installation-and-setup)⚙️ | [Usage of ClickNSend](#usage-of-clicknsend)🏃| [Presentation Video](#presentation-video)📹 | [Contact](#contact)📫 | [References](#references-and-other-software-tools)📖 
</div>

### Introduction <a name="introduction"></a>

**ClickNSend** is a Fusion 360 Add-In that streamlines the 3D printing workflow by allowing users to send selected bodies or components to their preferred slicer software with just a single click.

#### Motivation

The standard print utility in Fusion 360 (as of version 2.0.21538) lacks efficient functionality for exporting multiple selected bodies or components directly to third-party slicers like Orca Slicer for downstream 3D printing operations. This limitation creates friction in the design-to-print workflow, especially when working with complex multi-body designs.

#### Benefits

- **Simplified Workflow**: Send any selection of bodies or components directly to your slicer with a single click
- **Time-Saving**: Eliminate the need for manual STL export and import processes
- **Seamless Integration**: Adds a convenient 3D printer icon to your Fusion 360 Insert panel
- **Customizable**: Works with your preferred slicer software (default: Orca Slicer)
- **Multi-Selection Support**: Export single or multiple geometries simultaneously

Once installed, ClickNSend integrates directly into your Fusion 360 interface, providing an intuitive one-click solution for sending your designs to your favorite slicer software.

### Folder Structure of the Repository <a name="folder-structure-of-the-repository"></a>

<details>
<summary>Click to expand Folder Structure of the Repository</summary>

```ClickNSend/
├── commands/               # Command implementations
│   ├── __pycache__/        # Python cache for commands
│   ├── commandDialog/      # UI dialog components
│   └── __init__.py         # Commands initialization
├── lib/                    # Library files
│   └── fusionAddInUtils/   # Fusion 360 Add-In utilities
├── AddInIcon.svg           # Add-In icon for Fusion 360
├── ClickNSend.manifest     # Add-In manifest file
├── ClickNSend.py           # Main Add-In entry point
├── LICENSE                 # MIT License file
├── README.md               # This file
└── config.py               # Configuration settings
```

</details>

### Installation and Setup <a name="installation-and-setup"></a>

<details>
<summary>Click to expand Installation and Setup</summary>

1. Start Fusion 360 and click `Utilities` and `Scripts and Add-Ins` (or press `Shift+S` on Windows).
![Fusion360_MWHySdwzPN](https://github.com/user-attachments/assets/d7297c58-c862-4caa-b3af-4c2d90b38292)
![Fusion360_IQ7TtftQDs](https://github.com/user-attachments/assets/384f651b-8479-4382-bd3c-f5208aef79a5)

2. Once the `Script and Add-Ins` opened, click on the `Add-Ins` tab and click the green ➕ icon at the top. This will help you locate your Add-Ins folder. Note the folder path displayed and copy it for reference.
![Fusion360_MUjPGD653B](https://github.com/user-attachments/assets/547c0e1a-0e40-4353-8ca7-af8996bae7b0)

3. Go to GitHub and download `ClickNSend` as a ZIP file, then extract it to your Add-Ins folder (the location you noted in Step 2). You can remove `-main` from the end of the folder if you want to have only `ClickNSend` in your Add-Ins.
![Fusion360_SWeHkOoxGB](https://github.com/user-attachments/assets/15f50c07-d8e6-4534-aed1-7777bee9d516)

4. Return to Fusion 360 and navigate to the Add-Ins tab (repeat Step 1). You should now see `ClickNSend` in your list of available Add-Ins. Select it and click "Run" at the bottom.
![Fusion360_RxQlbhzfp4](https://github.com/user-attachments/assets/ffac7848-9f20-4f20-bb63-1d56bc5f5b57)

__Note:__ If you want ClickNSend to launch automatically whenever you start Fusion 360, check the box labeled `Run on Startup` before clicking Run.
![Fusion360_9AHoh0Iw5t](https://github.com/user-attachments/assets/f3d237b7-fdc4-46c8-9203-f6707f29f547)

5. You should see something similar in your `InsertPanel`.
![Fusion360_cUFjQkscWg](https://github.com/user-attachments/assets/4beaa395-48d5-4e13-aea2-add79c525758)

</details>

### Usage of ClickNSend <a name="usage-of-clicknsend"></a>

<details>
<summary>Click to expand Usage of ClickNSend</summary>

1. With your models open in the active window of Fusion 360, select the bodies that you want to send to the slicer. (e.g., sample Cube and Rectangular Box below)
![Fusion360_K07RrYpt1P](https://github.com/user-attachments/assets/455bb081-7335-45b4-b099-2708c0dbbc24)

2. Click on the `ClickNSend` icon (3D printer icon in your Fusion 360 Insert panel). That's it! Each selected body will be sent separately to your target slicer with its default settings.

Single Body:
![Fusion360_nUtPGZ4SRt](https://github.com/user-attachments/assets/03a7120d-08e9-4306-b0a7-48ccfe0c3b56)
![EQeUZfO25L](https://github.com/user-attachments/assets/0d38c83d-e902-4a51-86a2-5f25130f290a)

Multiple Bodies:
![Fusion360_beVK8jCO7B](https://github.com/user-attachments/assets/7a115d7e-2e1b-4131-947d-5d5f7048d1cb)
![ll8fckRHFy](https://github.com/user-attachments/assets/0c34e3db-9f8e-4789-885a-ea942264733e)

__Note:__  
**1-** The add-in does not include any 3D packing or size verification to check whether objects will fit on your 3D printer's build plate. It assumes you are familiar with your 3D printer's dimensions and capabilities. Since the code is open-source, you're welcome to modify it to add these features if needed.  
**2-** Once you send multiple bodies to Orca Slicer, you need to adjust their positions and orientations inside Orca (or your own Slicer). Currently, there is no effort to optimize it from my side. (Please see the end of the former note.)

</details>

### Presentation Video <a name="presentation-video"></a>
<a href="https://youtu.be/7a8Z9qCItDY">
    <img src="https://github.com/user-attachments/assets/e75340d7-da48-4b0d-aec2-30e0bb146eec" alt="Presentation4">
</a>

### Contact <a name="contact"></a>

For questions or contributions, please contact:
- Email: sinan.bank@colostate.edu

### References and Other Software Tools <a name="references-and-other-software-tools"></a>

- [Fusion 360](https://www.autodesk.com/products/fusion-360/overview) - 3D CAD, CAM, and CAE software.  
- [Fusion 360 API](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A) - Documentation of Application Programming interface of Fusion 360.  
- [Orca Slicer](https://github.com/SoftFever/OrcaSlicer) - A 3D printing slicer based on Bambu Studio, PrusaSlicer, and SuperSlicer.
- [Create A Custom Add-in To Send To 3D Print Utility](https://www.youtube.com/watch?v=9tiyAdgTzyI) - Similar Add-In for single body/ component import.



