"""
Draw the Convex Hull of Given Points
SEE: https://www.designcoding.net/convex-hull-with-rhino-python/
"""
import rhinoscriptsyntax as rs

def main(points, plane, close_hull=True):
  if not points:
    return False

  if not plane:
    return False

  plane_x = 0
  plane_y = 1

  current = min(points)
  start = current
  hull = []

  while current:
    origin = current
    current = points[0]
    for candidate in points:
      if (current[plane_x] - origin[plane_x]) * (candidate[plane_y] - origin[plane_y]) - (current[plane_y] - origin[plane_y]) * (candidate[plane_x] - origin[plane_x]) < 0:
        current = candidate
    hull.append(current)
    if current == start:
      break

  if close_hull:
    hull.append(hull[0])

  return hull

def rhino():
  points = rs.GetPointCoordinates("Select points", preselect=True)
  if not points:
    return

  plane = rs.ViewCPlane()
  if not plane:
    return

  hull = main(points, plane, close_hull=True)
  if hull:
    rs.AddPolyline(hull)

if __name__ == '__main__':
  rhino()
