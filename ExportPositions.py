"""Export object positions"""
import rhinoscriptsyntax as rs

def export_as_points():
  """export_as_points"""
  objs = rs.GetObjects("Select objects to export", 0, True, True)
  if not objs:
    return

  filename = rs.SaveFileName("Save CSV file", "*.csv||", None, "points.csv", "csv")
  csv = open(filename, 'w')
  headerline = "x,y,z\n"
  csv.write(headerline)

  for obj in objs:
    box = rs.BoundingBox(obj)
    center = (box[0] + box[6]) / 2
    x = center[0]
    y = center[1]
    z = center[2]
    csv.write("%.4f,%.4f,%.4f \n" %(x, y, z))
  csv.close()

if __name__ == '__main__':
  export_as_points()
