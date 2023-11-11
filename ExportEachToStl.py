"""Export selected objects to STL file, grouped by layer name"""
import os
import re
import unicodedata
import rhinoscriptsyntax as rs

def slugify(value):
  """
  Converts to lowercase, removes non-word characters (alphanumerics and
  underscores) and converts spaces to hyphens. Also strips leading and
  trailing whitespace.
  """
  value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
  value = re.sub('[^\w\s-]', '', value).strip().lower()
  return re.sub('[-\s]+', '-', value)

def export_each_to_stl():
  """export_each_to_stl"""
  objects = rs.GetObjects("Select objects to export", 0, True, True)
  if not objects:
    return

  layers = {}
  ns = os.path.splitext(os.path.basename(rs.DocumentName()))[0] + '_'

  for obj in objects:
    layer = rs.ObjectLayer(obj)

    id = rs.LayerName(layer)
    if id not in layers:
      layers[id] = []

    layers[id].append(obj)

  for layer, objects in layers.items():
    filename = rs.SaveFileName("Export object file", "*.stl||", None, ns + slugify(layer) + ".stl", "stl")
    if not filename:
      continue

    rs.UnselectAllObjects()
    rs.SelectObjects(objects)
    rs.Command("_-Export " + chr(34) + filename + chr(34) + " _Enter", False)

if __name__ == '__main__':
  export_each_to_stl()
