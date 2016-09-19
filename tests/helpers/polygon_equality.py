from shapely.geometry.collection import GeometryCollection
from shapely.geometry.polygon import Polygon

def _mkpoly(coords):
    return Polygon(list(coords) + [coords[0]])

def check_equality_issues(polygon, triangles):
    s_polygon = Polygon(polygon)

    polygon_area = s_polygon.area
    triangles_area = 0

    print("Check")
    union = GeometryCollection([])
    for triangle in triangles:
        s_triangle = Polygon(triangle)
        triangles_area += s_triangle.area
        union = union.union(s_triangle)
        print(s_triangle, union)

    issues = []
    if triangles_area > polygon_area + 1E-6:
        issues.append("Triangle area > Poylgon area")

    if triangles_area < polygon_area - 1E-6:
        issues.append("Triangle area > Poylgon area")

    if union.difference(s_polygon).area > 1E-6:
        issues.append("Triangles go outside polygon")

    if s_polygon.difference(union).area > 1E-6:
        issues.append("Triangles does not cover polygon")

    return issues