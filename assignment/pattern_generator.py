import maya.cmds as cmds
# This imports maya comands and comands

cmds.file(new=True, force=True)
# This forces a new file to be created

def generate_pattern():
    num_rows = 6        
    num_cols = 6        
    spacing = 3.0    
# This picks the number of rows,columns, and spacing    

    for row in range(num_rows):
        for col in range(num_cols):
            x_pos = col * spacing
            z_pos = row * spacing
# This determines the spacing of the pattern and essentially creates the pattern
            if (row + col) % 2 == 0:
                object = cmds.polyCube(
                    width = 2,
                    height = 2,
                    depth = 2
                    )[0]
                cmds.move(0,1,0,object)
# This creates the cube
            else:
                object = cmds.polySphere(
                radius = 1
                )[0]
            cmds.move(0,1,0,object)
# This creates the sphere
            cmds.move(x_pos,0,z_pos,object)

generate_pattern()


cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
# If everything is in the viewport then it prints the message
