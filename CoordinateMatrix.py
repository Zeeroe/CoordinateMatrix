def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def grid_add():
    global grid, temp_grid
    grid.append(temp_grid)
    temp_grid = []


grid = []
temp_grid = []

INPUT_SIZE = 4  # number of points per row and column
res = INPUT_SIZE - 1

topleft = (20, 0)
topright = (80, 0)
bottomright = (100, 100)
bottomleft = (0, 100)

corners = [topleft, topright, bottomright, bottomleft]

# get points along each side
sides = []
for j in range(4):
    temp_points = []
    for i in range(res-1):
        ratio = (i + 1) * (1 / res)
        Px = corners[j][0] * (1 - ratio) + corners[(j + 1) % 4][0] * ratio
        Py = corners[j][1] * (1 - ratio) + corners[(j + 1) % 4][1] * ratio
        Px = round(Px)
        Py = round(Py)
        temp_points.append((Px, Py))
    if j < 2:
        sides.append(temp_points)
    else:
        temp_points.reverse()
        sides.append(temp_points)

print("0 TL-TR:", sides[0], "\n1 TR-BR:", sides[1], "\n2 BR-BL:", sides[2], "\n3 BL-TL:", sides[3])

#
h_lines = []
v_lines = []
for k in range(res - 1):
    h_lines.append((sides[3][k], sides[1][k]))
    v_lines.append((sides[0][k], sides[2][k]))

# print("h_lines:", h_lines, "\nv_lines:", v_lines)

#
intersections = []
for p in range(len(h_lines)):
    temp_inter = []
    for q in range(len(v_lines)):
        line1 = h_lines[p]
        line2 = v_lines[q]
        dx = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        dy = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
        divi = det(dx, dy)
        if divi == 0:
            raise Exception
        dete = (det(*line1), det(*line2))
        x = det(dete, dx) / divi
        y = det(dete, dy) / divi
        x = round(x)
        y = round(y)
        temp_inter.append((x, y))
    intersections.append(temp_inter)

# print(intersections)

# adding all points gathered into a list
# first row
temp_grid.append(topleft)
for m in sides[0]:
    temp_grid.append(m)
temp_grid.append(topright)
grid_add()

# middle rows
for n in range(len(sides[3])):
    temp_grid.append(sides[3][n])
    for o in intersections[n]:
        temp_grid.append(o)
    temp_grid.append(sides[1][n])
    grid_add()

# last row
temp_grid.append(bottomleft)
for s in sides[2]:
    temp_grid.append(s)
temp_grid.append(bottomright)
grid_add()

print(grid)
