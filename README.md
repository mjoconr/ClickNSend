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
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/fa33e860-1219-4ee7-be45-ec94c3fd5ed9" alt="Fusion360_MWHySdwzPN">
    </td>
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/b8043e39-ee93-4983-9c6a-c30b2249a2d2" alt="Fusion360_IQ7TtftQDs">
    </td>
  </tr>
</table>

2. Once the `Script and Add-Ins` opened, click on the `Add-Ins` tab and click the green ➕ icon at the top. This will help you locate your Add-Ins folder. Note the folder path displayed and copy it for reference.
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/a7af1886-e3e0-485b-b139-e847bad42c81" alt="Fusion360_ZQlCPHgSZn">
    </td>
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/d4b58c61-3b39-46b3-94dc-d926604ab85a" alt="Fusion360_SWeHkOoxGB">
    </td>
  </tr>
</table>

3. Go to GitHub and download `ClickNSend` as a ZIP file, then extract it to your Add-Ins folder (the location you noted in Step 2). You can remove `-main` from the end of the folder if you want to have only `ClickNSend` in your Add-Ins.
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/8fb5481e-d3a7-4e2b-8326-4a1338dda1f4" alt="chrome_rCk0vdemUi">
    </td>
  </tr>
</table>

4. Return to Fusion 360 and navigate to the Add-Ins tab (repeat Step 1). You should now see `ClickNSend` in your list of available Add-Ins. Select it and click "Run" at the bottom.
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/db7f755c-5ba5-453d-acd3-30e0eb9ce238" alt="Fusion360_RxQlbhzfp4">
    </td>
  </tr>
</table>

__Note:__ If you want ClickNSend to launch automatically whenever you start Fusion 360, check the box labeled `Run on Startup` before clicking Run.
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/83f2bf59-e84e-4ac4-9d01-ff5c94fb1a19" alt="Fusion360_9AHoh0Iw5t">
    </td>
  </tr>
</table>

5. You should see something similar in your `InsertPanel`.
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/f321534e-77fc-4cb8-ac9c-d726e3a3903e" alt="Fusion360_cUFjQkscWg">
    </td>
  </tr>
</table>

</details>

### Usage of ClickNSend <a name="usage-of-clicknsend"></a>

<details>
<summary>Click to expand Usage of ClickNSend</summary>

1. With your models open in the active window of Fusion 360, select the bodies that you want to send to the slicer. (e.g., sample Cube and Rectangular Box below)
![Fusion360_K07RrYpt1P](https://github.com/user-attachments/assets/f1b12a16-142d-415e-a1f3-786c72dd20f0)

2. Click on the `ClickNSend` icon (3D printer icon in your Fusion 360 Insert panel). That's it! Each selected body will be sent separately to your target slicer with its default settings.

Single Body:
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/688b3d5c-000b-442f-9f92-c682f53091ec" alt="Fusion360_nUtPGZ4SRt">
    </td>
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/198c08ec-f2e9-4cd3-9f86-3fb2d7c39899" alt="EQeUZfO25L">
    </td>
  </tr>
</table>

Multiple Bodies:
<table style="border: none;">
  <tr style="border: none;">
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/9869ca10-3676-4845-ac10-ebc06586afe2" alt="Fusion360_beVK8jCO7B">
    </td>
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/1aa0f7e4-c012-4007-9bcc-db7ca95e9ca0" alt="ll8fckRHFy">
    </td>
  </tr>
</table>

__Note:__ 
**1-** The add-in does not include any 3D packing or size verification to check whether objects will fit on your 3D printer's build plate. It assumes you are familiar with your 3D printer's dimensions and capabilities. Since the code is open-source, you're welcome to modify it to add these features if needed.  
**2-** Once you send multiple bodies to Orca Slicer, you need to adjust their positions and orientations inside Orca (or your own Slicer). Currently, there is no effort to optimize it from my side. (Please see the end of the former note.)

</details>

### Presentation Video <a name="presentation-video"></a>

Coming soon! A video demonstration of the ClickNSend Add-In will be added here.

### Contact <a name="contact"></a>

For questions or contributions, please contact:
- GitHub: sinan.bank@colostate.edu

### References and Other Software Tools <a name="references-and-other-software-tools"></a>

- [Fusion 360](https://www.autodesk.com/products/fusion-360/overview) - 3D CAD, CAM, and CAE software.  
- [Fusion 360 API](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A) - Documentation of Application Programming interface of Fusion 360.  
- [Orca Slicer](https://github.com/SoftFever/OrcaSlicer) - A 3D printing slicer based on Bambu Studio, PrusaSlicer, and SuperSlicer.
- [Create A Custom Add-in To Send To 3D Print Utility](https://www.youtube.com/watch?v=9tiyAdgTzyI) - Similar Add-In for single body/ component import.



