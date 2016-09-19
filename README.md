polytri
=======

Python 3 algorithm to turn polygons into triangles.

 * Convex and non-convex polygons are supported.
 * Polygon vertices must all be within a single plane, but the
   polygon itself may exist in 2 or 3 dimensional space
 * Clockwise and counter-clockwise winding supported.
 * Inverted polygons and polygons with holes are NOT supported.
 * Given many possible triangulations of a polygon, this algorithm
   does not make any attempt to pick a better one (for any definition
   of 'better').

## Requirements

Requires numpy.  Shapely and pytest for testing.