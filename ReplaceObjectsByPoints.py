"""replace_objects_by_points"""
import rhinoscriptsyntax as rs

def replace_objects_by_points():
  """replace_objects_by_points"""
  objs = rs.GetObjects("Select objects to transform to points", 0, True, True)
  if not objs:
    return

  for obj in objs:
    box = rs.BoundingBox(obj)
    center = (box[0] + box[6]) / 2
    rs.AddPoint(center)
    rs.DeleteObject(obj)

if __name__ == '__main__':
  replace_objects_by_points()
