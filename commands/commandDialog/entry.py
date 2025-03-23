import adsk.core
import os
import tempfile
import subprocess
import platform
from ...lib import fusionAddInUtils as futil
from ... import config

app = adsk.core.Application.get()
ui = app.userInterface

CMD_ID=f'{config.COMPANY_NAME}_{config.ADDIN_NAME}_entry'
CMD_NAME='Send Geometry to Orca Slicer'
CMD_DESCRIPTION='A Fusion Add-in That sends selected bodies/ components to Orca Slicer'

# Specify that the command will be promoted to the toolbar
IS_PROMOTED = True

# Define the location where the command button will be created
WORKSPACE_ID = 'FusionSolidEnvironment'
PANEL_ID = 'InsertPanel'
COMMAND_BESIDE_ID= ''

# Resource location for command icons, here we assume a sub folder in this directory named 'resources'
ICON_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', '')

# Local list of event handlers used to maintain a reference so
# they are not released and garbage collected
local_handlers = []

# Executed when add-in is started
def start():
    # Create a command definition
    cmd_def = ui.commandDefinitions.addButtonDefinition(CMD_ID, CMD_NAME, CMD_DESCRIPTION, ICON_FOLDER)

    # Define an event handler for the command created event. It will be called when the button is clicked.
    futil.add_handler(cmd_def.commandCreated, command_created)

    # Add a button into the UI so user can click it
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    # Get the panel the button will be added to
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    # Create button control
    control = panel.controls.addCommand(cmd_def, COMMAND_BESIDE_ID)
    # Specify if the button is promoted
    control.isPromoted = IS_PROMOTED

# Executed when add-in is stopped
def stop():
    # Get various UI elements for this command
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    command_control = panel.controls.itemById(CMD_ID)
    command_definition = ui.commandDefinitions.itemById(CMD_ID)

    # Delete the button command control
    if command_control:
        command_control.deleteMe()
    
    # Delete the command definition
    if command_definition:
        command_definition.deleteMe()
    
# Function that is called that is called when a user clicks the corresponding button in the UI.
def command_created(args: adsk.core.CommandEventArgs):
    # General logging debugging
    futil.log(f'Command Created: {CMD_ID}')

    try:
        # Get active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        # Get the root component in this design
        rootComp = design.rootComponent
        
        # Check for selected components or bodies
        selectedComponents = []
        selectedBodies = []
        selectedOccurrences = []
        
        # Get the current selection
        selection = ui.activeSelections
        
        # Check each selected item to see if it's a component or body
        if selection and selection.count > 0:
            futil.log(f'Number of selected items: {selection.count}')
            
            for i in range(selection.count):
                selected = selection.item(i)
                futil.log(f'Selection type: {selected.entity.objectType}')
                
                # Check if it's a component
                if hasattr(adsk.fusion, 'Component') and selected.entity.objectType == adsk.fusion.Component.classType():
                    selectedComponents.append(selected.entity)
                    futil.log(f'Selected component: {selected.entity.name}')
                
                # Check if it's a body
                elif hasattr(adsk.fusion, 'BRepBody') and selected.entity.objectType == adsk.fusion.BRepBody.classType():
                    selectedBodies.append(selected.entity)
                    futil.log(f'Selected body: {selected.entity.name}')
                
                # Check for occurrence which contains a component
                elif hasattr(adsk.fusion, 'Occurrence') and selected.entity.objectType == adsk.fusion.Occurrence.classType():
                    occurrence = adsk.fusion.Occurrence.cast(selected.entity)
                    selectedOccurrences.append(occurrence)
                    futil.log(f'Selected occurrence: {occurrence.name}')
        
        # Create a temporary directory to store STL files
        temp_dir = tempfile.mkdtemp()
        futil.log(f'Created temporary directory: {temp_dir}')
        
        # Create the export manager
        exportMgr = design.exportManager
        
        # Detect OS and set Orca Slicer path accordingly
        system = platform.system()
        if system == 'Darwin':  # macOS
            orcaPath = "/Applications/OrcaSlicer.app/Contents/MacOS/orca-slicer"
            # orcaPath = "/Applications/BambuStudio.app/Contents/MacOS/bambu-studio" # For Bambu Studio
            futil.log(f'Detected macOS: Using Orca Slicer path: {orcaPath}')
        else:  # Windows or other
            orcaPath = r"C:\Program Files\OrcaSlicer\orca-slicer.exe"
            # orcaPath = r"C:\Program Files\Bambu Studio\bambu-studio.exe" # For bambu studio
            futil.log(f'Detected {system}: Using Orca Slicer path: {orcaPath}')
        
        # List to store all STL file paths
        stl_files = []
        
        # Export selected entities or fall back to root component
        if len(selectedComponents) > 0 or len(selectedBodies) > 0 or len(selectedOccurrences) > 0:
            # If components or bodies are selected, export only those
            bodiesExported = 0
            
            # Export components directly - but export each body individually to preserve separation
            if len(selectedComponents) > 0:
                futil.log(f'Exporting {len(selectedComponents)} selected component(s) as separate bodies')
                for component in selectedComponents:
                    if component != rootComp:  # Don't export the root component directly
                        try:
                            # Export each body in the component separately
                            for body in component.bRepBodies:
                                stl_file = os.path.join(temp_dir, f"{body.name}_{bodiesExported}.stl")
                                stlOptions = exportMgr.createSTLExportOptions(body, stl_file)
                                if export_to_stl(exportMgr, stlOptions):
                                    stl_files.append(stl_file)
                                    bodiesExported += 1
                                    futil.log(f'Successfully exported body: {body.name} from component: {component.name}')
                        except Exception as e:
                            futil.log(f'Error exporting component {component.name}: {str(e)}')
            
            # Export occurrences - but export each body individually to preserve separation
            if len(selectedOccurrences) > 0:
                futil.log(f'Exporting {len(selectedOccurrences)} selected occurrence(s) as separate bodies')
                for occurrence in selectedOccurrences:
                    try:
                        # Export each body in the occurrence separately
                        for body in occurrence.bRepBodies:
                            stl_file = os.path.join(temp_dir, f"{body.name}_{bodiesExported}.stl")
                            stlOptions = exportMgr.createSTLExportOptions(body, stl_file)
                            if export_to_stl(exportMgr, stlOptions):
                                stl_files.append(stl_file)
                                bodiesExported += 1
                                futil.log(f'Successfully exported body: {body.name} from occurrence: {occurrence.name}')
                    except Exception as e:
                        futil.log(f'Error exporting occurrence {occurrence.name}: {str(e)}')
            
            # Export bodies - already individual
            if len(selectedBodies) > 0:
                futil.log(f'Exporting {len(selectedBodies)} selected body(s)')
                for body in selectedBodies:
                    try:
                        stl_file = os.path.join(temp_dir, f"{body.name}_{bodiesExported}.stl")
                        stlOptions = exportMgr.createSTLExportOptions(body, stl_file)
                        if export_to_stl(exportMgr, stlOptions):
                            stl_files.append(stl_file)
                            bodiesExported += 1
                            futil.log(f'Successfully exported body: {body.name}')
                    except Exception as e:
                        futil.log(f'Error exporting body {body.name}: {str(e)}')
            
            if bodiesExported > 0:
                # Launch Orca Slicer with all exported STL files
                launch_orca_slicer(orcaPath, stl_files)
                ui.messageBox(f'Exported {bodiesExported} bodies to Orca Slicer', 'Export Complete')
            else:
                ui.messageBox('Unable to export the selected items. Please check the log for details.', 'Export Failed')
        else:
            # No selection, export all bodies from the root component individually
            futil.log('No components or bodies selected, exporting all bodies from root component individually')
            try:
                bodiesExported = 0
                allBodies = rootComp.bRepBodies
                futil.log(f'Found {allBodies.count} bodies in root component')
                
                for i in range(allBodies.count):
                    body = allBodies.item(i)
                    stl_file = os.path.join(temp_dir, f"{body.name}_{i}.stl")
                    futil.log(f'Exporting body {i+1}/{allBodies.count}: {body.name}')
                    
                    stlOptions = exportMgr.createSTLExportOptions(body, stl_file)
                    if export_to_stl(exportMgr, stlOptions):
                        stl_files.append(stl_file)
                        bodiesExported += 1
                        futil.log(f'Successfully exported body: {body.name}')
                
                if bodiesExported > 0:
                    # Launch Orca Slicer with all exported STL files
                    launch_orca_slicer(orcaPath, stl_files)
                    ui.messageBox(f'Exported {bodiesExported} bodies from root component to Orca Slicer', 'Export Complete')
                else:
                    ui.messageBox('No bodies were exported from root component', 'Export Failed')
            except Exception as e:
                futil.log(f'Error exporting bodies from root component: {str(e)}')
                ui.messageBox(f'Error exporting bodies from root component: {str(e)}', 'Export Failed')
            
    except Exception as e:
        futil.log(f'Failed to export: {str(e)}')
        ui.messageBox(f'Failed to export: {str(e)}', 'Error')

# Helper function to export a selection to an STL file
def export_to_stl(exportMgr, stlOptions):
    try:
        # Set mesh refinement if supported
        try:
            if hasattr(stlOptions, 'meshRefinement'):
                stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        except:
            pass
        
        # Execute the export
        result = exportMgr.execute(stlOptions)
        return result
    except Exception as e:
        futil.log(f'Export to STL failed with error: {str(e)}')
        return False

# Helper function to launch Orca Slicer with a list of STL files
def launch_orca_slicer(orca_path, stl_files):
    try:
        if not stl_files:
            futil.log('No STL files to open')
            return False
        
        futil.log(f'Launching Orca Slicer with {len(stl_files)} STL files')
        
        # Create the command based on OS
        system = platform.system()
        if system == 'Darwin':  # macOS
            if "BambuStudio" in orca_path:
                cmd = ["open", "-a", "BambuStudio", "--args"] + stl_files
                futil.log(f'macOS launch command for Bambu Studio: {cmd}')
            else:
                cmd = ["open", "-a", "OrcaSlicer", "--args"] + stl_files
                futil.log(f'macOS launch command for Orca Slicer: {cmd}')
        else:  # Windows or other
            cmd = [orca_path] + stl_files
            futil.log(f'{system} launch command: {cmd}')
        
        # Launch Orca Slicer with the STL files
        subprocess.Popen(cmd)
        return True
    except Exception as e:
        futil.log(f'Failed to launch Orca Slicer: {str(e)}')
        return False


