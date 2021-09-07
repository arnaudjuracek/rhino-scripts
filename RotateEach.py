"""Rotate each object separately, optionnaly w/ a random angle"""
import random as rng
import rhinoscriptsyntax as rs

def rotate_each_objects():
  """rotate_each_objects"""
  objs = rs.GetObjects("Select objects to rotate", 0, True, True)
  if not objs:
    return

  alpha = rs.GetInteger("Enter angle in degrees (leave 0 for a random angle)", 0)
  use_random = (alpha == 0)


  for obj in objs:
    groups = rs.ObjectGroups(obj)
    group_name = None
    if groups:
      group_name = groups[0]

    box = rs.BoundingBox(rs.ObjectsByGroup(group_name) if group_name else obj)
    center = (box[0] + box[6]) / 2

    if use_random:
      alpha = rng.randrange(0, 360, 1)

    rs.RotateObject(obj, center, alpha, None, False)

if __name__ == '__main__':
  rotate_each_objects()
