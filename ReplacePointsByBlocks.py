"""replace_points_by_blocks"""
import rhinoscriptsyntax as rs

def replace_points_by_blocks():
  """replace_points_by_blocks"""
  points = rs.GetObjects("Select points to replace with a block", 1, True, True)
  if not points:
    return

  blocks = rs.BlockNames()
  if not blocks:
    return

  block = rs.ListBox(blocks, "Select block", "Replace Points")
  if not block:
    return

  rs.EnableRedraw(False)

  for point in points:
    rs.InsertBlock(block, point)

  rs.DeleteObjects(points)
  rs.EnableRedraw(True)

if __name__ == '__main__':
  replace_points_by_blocks()
