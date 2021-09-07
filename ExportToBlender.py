"""Export selected objects to obj optimized for Blender imports"""
import rhinoscriptsyntax as rs

def export_to_blender():
  """export_to_blender"""
  objects = rs.GetObjects("Select objects to export", 0, True, True)
  if not objects:
    return

  filename = rs.SaveFileName("Export objects file", "*.obj||", None, "blender.obj", "obj")
  if not filename:
    return

  # Get bbox of selection to define the new origin
  bbox = box = rs.BoundingBox(objects)
  if not bbox:
    return
  center = (box[0] + box[6] / 2)
  origin = rs.coerce3dpoint([0, 0, 0])

  # Run the script on a temporary clone of the selected objects
  objects = rs.CopyObjects(objects, center - origin)

  # Scale to meters
  scale = rs.UnitScale(4) # 4 is a pointer to the Meter unit
  objects = rs.ScaleObjects(objects, origin, (scale, scale, scale))

  mesh_queue = []
  meshes = []

  for obj in objects:
    layer = rs.ObjectLayer(obj)
    rs.ObjectName(obj, layer)

    # Assign a material based on object layer
    material = rs.AddMaterialToLayer(layer)
    rs.MaterialName(material, rs.LayerName(layer))
    rs.MaterialColor(material, rs.LayerColor(layer))

    # Queue object to mesh if needed
    if rs.IsMesh(obj):
      meshes.append(obj)
    else:
      mesh_queue.append(obj)

  # Convert to mesh
  if mesh_queue:
    rs.UnselectAllObjects()
    rs.SelectObjects(mesh_queue)
    rs.Command("!_-Mesh")
    meshes = meshes + rs.LastCreatedObjects()

  # Export
  rs.UnselectAllObjects()
  rs.SelectObjects(meshes)
  rs.Command("_-Export " + chr(34) + filename + chr(34) + " _Enter", False)

  # Clean up
  rs.DeleteObjects(objects)
  rs.DeleteObjects(meshes)

if __name__ == '__main__':
  export_to_blender()
