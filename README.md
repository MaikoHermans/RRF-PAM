# RRF-PAM
Print Area Mesh for RepRapFirmware

Adds dynamic mesh calibration to your RepRapFirmware printer.

- Should work out of the box on any RepRapFirmware
- respects all probe and mesh settings
- This script will also run G29 so it's not needed to do that separately anymore

# 1. Install
1. Copy the contents of the `print_area_mesh.g` file in the repo.
2. Move to your RRF interface and create a new file named `print_area_mesh.g` in `system`
3. Paste the content you copied in step 1.

# 2. Alterations
The file allows you to change a few things

`deviationFromOriginal`
This value determinens when the print area mesh will be activated.
If the print area is within the deviation from the original, the original probe settings will be upheld
Change this if you want the print area mesh to be activated at a different deviation

`minMeshPoints`
This value will determine the minimal amount of probe points that will be used

`maxMeshPoints`
This value will determine the maximum amount of probe ponts that will be used


# 3. Modify your slicers start print g-code
Replace your G29 command with the specified command for your slicer

- PrusaSlicer / SuperSlicer
```ini
M98 P"sys/print_area_mesh.g" A{first_layer_print_min[0]} B{first_layer_print_max[0]} C{first_layer_print_min[1]} D{first_layer_print_max[1]}
```

- Ideamaker 
```ini
M98 P"sys/print_area_mesh.g" A{print_pos_min_x} B{print_pos_max_x} C{print_pos_min_y} D{print_pos_max_y}
```

- Cura
```ini
M98 P"sys/print_area_mesh.g" A%MINX% B%MAXX% C%MINY% D%MAXY%
```

To make PAM work with Cura you need to install a post processing plugin

1. in cura open menu ```Help -> Show configuration folder```
2. copy [MeshPrintSize.py](/MeshPrintSize.py) into the ```scripts``` folder
3. restart cura
4. in cura open menu ```Extensions -> Post processing -> Modify G-Code``` and select ```Mesh Print Size```
