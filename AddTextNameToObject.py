"""add_text_name_to_object"""
import rhinoscriptsyntax as rs

def sort_by_name(obj):
  """sort_by_name"""
  name = rs.ObjectName(obj)
  return int(name[2:])

def add_text_name_to_object():
  """add_text_name_to_object"""
  objs = rs.GetObjects("Select objects to label", 0, False, True)
  if not objs:
    return

  height = rs.GetReal("Font height")
  if not height:
    return

  center = rs.GetPoint("Center of rotation")
  if not center:
    return

  origin = rs.GetPoint("Origin")
  if not origin:
    return

  end_angle = rs.GetAngle(
      point=center,
      reference_point=origin,
      default_angle_degrees=360,
      message="Angle max"
  )
  if not end_angle:
    return

  radius = rs.Distance([origin[0], origin[1], 0], [center[0], center[1], 0])
  start_angle = rs.Angle([center[0], center[1], 0], [origin[0], origin[1], 0])[0]

  rs.EnableRedraw(False)

  objs = sorted(objs, key=sort_by_name)

  for i in range(0, len(objs)): #pylint: disable=consider-using-enumerate
    obj = objs[i]
    name = rs.ObjectName(obj)
    if not name:
      continue

    name = name[2:]
    box = rs.BoundingBox(obj)
    text = rs.AddText(name, [center[0], center[1] + radius, box[4][2]], height, "Arial")
    rs.RotateObject(text, [center[0], center[1] + radius, box[4][2]], 180)

    alpha = start_angle + (i / len(objs)) * end_angle
    rs.RotateObject(text, [center[0], center[1], box[4][2]], alpha - 90)

    block = rs.AddBlock([obj, text], box[0], name=name, delete_input=True)
    rs.InsertBlock(block, box[0])

  rs.EnableRedraw(True)
  return

if __name__ == '__main__':
  add_text_name_to_object()
