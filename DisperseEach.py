"""Move randomly each object separately with a given max offset"""
import random as rng
import rhinoscriptsyntax as rs

def move_each_objects():
  """move_each_objects"""
  objs = rs.GetObjects("Select objects to disperse", 0, True, True)
  if not objs:
    return

  offset_x = rs.GetInteger("Enter max dispersion distance on X axis", 0)
  offset_y = rs.GetInteger("Enter max dispersion distance on Y axis", 0)
  offset_z = rs.GetInteger("Enter max dispersion distance on Z axis", 0)


  for obj in objs:
    rs.MoveObject(obj, [
        0 if offset_x == 0 else rng.randrange(offset_x * -1, offset_x, 1),
        0 if offset_y == 0 else rng.randrange(offset_y * -1, offset_y, 1),
        0 if offset_z == 0 else rng.randrange(offset_z * -1, offset_z, 1)
    ])

if __name__ == '__main__':
  move_each_objects()
