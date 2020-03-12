"""
Draw the Convex Hull of Given Points
SEE: https://www.designcoding.net/convex-hull-with-rhino-python/
"""
import rhinoscriptsyntax as rs

def main():
  points = rs.GetPointCoordinates("Select points")
  if not points:
    return

  a = min(points)
  start = a

  while a:
    o = a
    a = points[0]
    for b in points:
      if (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]) < 0:
        a = b
    rs.AddLine(o, a)
    if a == start:
      break
  return

if __name__ == '__main__':
  main()
