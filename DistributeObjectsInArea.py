"""distribute_objects_in_area"""
import rhinoscriptsyntax as rs

def distribute_objects_in_area():
  """distribute_objects_in_area"""
  objs = rs.GetObjects("Select objects to place", 0, True, True)
  if not objs:
    return

  rect = rs.GetRectangle(0)
  if not rect:
    return

  margin = rs.GetInteger("Enter margin between slices", number=10, minimum=0)
  if not margin:
    return

  prev = rect[0]
  for obj in objs:
    start = rs.BoundingBox(obj)[0]
    vec = rs.PointSubtract(prev, start)
    rs.MoveObject(obj, vec)

    prev = rs.PointAdd(rs.BoundingBox(obj)[1], [margin, 0, 0])

    if prev[0] > rect[1][0]:
      prev = rect[0]
      origin = rs.BoundingBox(obj)[3]
      prev[1] = origin[1] + margin

if __name__ == '__main__':
  distribute_objects_in_area()
