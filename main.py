Web VPython 3.2

scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.green)
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.green)
wallB = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.green)
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.green)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball = sphere (color = color.green, radius = 0.4, make_trail=True, retain=200)
ball.mass = 1.0
ball.p = vector (-0.15, -0.23, +0.27)


