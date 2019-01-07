"""Generate N random points inside a given Box"""
import random
import rhinoscriptsyntax as rs

def main(box, n):
  if not box or not n:
    raise ValueError('Box or Length undefined')

  points = []
  for _ in range(0, n):
    x = random.uniform(box[0][0], box[6][0])
    y = random.uniform(box[0][1], box[6][1])
    z = random.uniform(box[0][2], box[6][2])
    points.append((x, y, z))

  return points

def rhino():
  box = rs.GetBox()
  if not box:
    return

  length = rs.GetInteger("Enter length of points")
  if not length:
    return

  points = main(box, length)
  for point in points:
    rs.AddPoint(point)

if __name__ == '__main__':
  rhino()
