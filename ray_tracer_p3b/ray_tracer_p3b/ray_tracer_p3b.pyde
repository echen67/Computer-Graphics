# This is the starter code for the CS 3451 Ray Tracing project.
#

# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

# Emily Chen

class create_scene():
    def __init__(self, fov, bg):
        self.fov = fov    # field of view, int
        self.bg = bg      # background color, PVector

class create_light():
    def __init__(self, pos, col):
        self.pos = pos    # location, PVector
        self.col = col    # color, PVector
        
class create_surface():
    def __init__(self, diff, amb, spec, p, krefl):
        self.diff = diff    # diffuse, PVector
        self.amb = amb      # ambient, PVector
        self.spec = spec    # specular, PVector
        self.p = p          # Phong exponent, int
        self.krefl = krefl  # reflection coefficient, int
        
class create_ray():
    def __init__(self, orig, dir):
        self.orig = orig    # origin, PVector
        self.dir = dir      # direction, PVector
        
class create_hit():
    def __init__(self, t, pos, id, n, type):
        self.t = t        # time, int
        self.pos = pos    # where the ray intersects the object, PVector
        self.id = id      # id of the object that was hit, int
        self.n = n        # normal, PVector
        self.type = type

class create_sphere():    
    def __init__(self, radius, center, id, surface, type):
        self.center = center    # sphere center, PVector
        self.radius = radius    # sphere radius, int
        self.id = id            # position in the spheres list, int
        self.surface = surface  # position of the corresponding surface in the surfaces list, int
        self.type = type        # is this a sphere or triangle

class create_triangle():
    def __init__(self, v1, v2, v3, id, surface, type):
        self.v1 = v1    # first vertex, PVector
        self.v2 = v2    # second vertex, PVector
        self.v3 = v3    # third vertex, PVector
        self.id = id
        self.surface = surface    # position of corresponding surface
        self.type = type          # is this a sphere or triangle        

def setup():
    size(200, 200) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global scene    # fov & bg color
    scene = create_scene(0, PVector(0,0,0))
    
    global spheres    # list of spheres
    spheres = []
    
    global lightList    # list of lights
    lightList = []
    
    global surfaces    # list of surfaces
    surfaces = []
    
    global currentSurface    # surface to assign to the next object
    currentSurface = None
    
    global triangles    # list of triangles
    triangles = []
    
    triVerts = []    # keep track of the next three vertices, which will then be assigned to a triangle
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            center = PVector(x,y,z)
            id = len(spheres)
            aSphere = create_sphere(radius, center, id, currentSurface, "s")
            spheres.append(aSphere)
        elif words[0] == 'fov':
            scene.fov = words[1]
        elif words[0] == 'background':
            scene.bg = PVector(float(words[1]), float(words[2]), float(words[3]))
        elif words[0] == 'light':
            pos = PVector(float(words[1]), float(words[2]), float(words[3]))
            col = PVector(float(words[4]), float(words[5]), float(words[6]))
            light = create_light(pos, col)
            lightList.append(light)
        elif words[0] == 'surface':
            diff = PVector(float(words[1]), float(words[2]), float(words[3]))
            amb = PVector(float(words[4]), float(words[5]), float(words[6]))
            spec = PVector(float(words[7]), float(words[8]), float(words[9]))
            p = float(words[10])
            krefl = float(words[11])
            surface = create_surface(diff, amb, spec, p, krefl)
            surfaces.append(surface)
            currentSurface = len(surfaces)-1
        elif words[0] == 'begin':
            triVerts = []
        elif words[0] == 'vertex':
            vert = PVector( float(words[1]), float(words[2]), float(words[3]) )
            triVerts.append(vert)
        elif words[0] == 'end':
            tri = create_triangle( triVerts[0], triVerts[1], triVerts[2], len(triangles), currentSurface, "t" )
            triangles.append(tri)
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    print("START")
    orig = PVector(0,0,0)
    global scene
    fov = float(scene.fov)
    k = tan(radians(fov/2))
    global spheres
    global surfaces
    global lightList
    
    global i
    global j
    for j in range(height):
        for i in range(width):
            # create an eye ray for pixel (i,j) and cast it into the scene
            newX = i*((2*k)/width) - k
            newY = j*((2*k)/height) - k
            dir = PVector(newX, -newY, -1)
            #dir.normalize()
            eyeRay = create_ray(orig, dir)
            
            #Loop through objects and see if ray intersects with them
            sphereHit = intersect_sphere(eyeRay)
            triHit = intersect_triangle(eyeRay) 
            
            nearestHit = create_hit(-1, None, 0, None, "")
        
            if sphereHit.t > 0 and triHit.t < 0:
                nearestHit = sphereHit
            elif triHit.t > 0 and sphereHit.t < 0:
                nearestHit = triHit
            elif sphereHit.t > 0 and triHit.t > 0 and sphereHit.t > triHit.t:
                nearestHit = sphereHit
            # elif sphereHit.t > 0 and triHit.t > 0 and sphereHit.t < triHit.t:
            #     nearestHit = triHit

            #Now find the correct color for that pixel
            pix_color = shading(nearestHit, eyeRay, 0)
            set (i, j, pix_color)
            
    print("DONE")

# should remain empty for this assignment
def draw():
    # print(mouseX, mouseY)
    pass
    
# use shading equation
def shading(nearestHit, eyeRay, rec):
    if rec > 10:
        return color(0,0,0)
    if nearestHit.t >= 0:
        if nearestHit.type == "s":
            surfacepos = spheres[nearestHit.id].surface
        else:
            surfacepos = triangles[nearestHit.id].surface
        surface = surfaces[surfacepos]
        
        N = nearestHit.n
        N.normalize()
        
        P = surface.p
        
        # Diffuse
        Dr = surface.diff.x
        Dg = surface.diff.y
        Db = surface.diff.z
        
        # Ambient
        Ar = surface.amb.x
        Ag = surface.amb.y
        Ab = surface.amb.z
        
        # Specular
        Sr = surface.spec.x
        Sg = surface.spec.y
        Sb = surface.spec.z
        
        # Summation of all lights
        lightRed = 0
        lightGreen = 0
        lightBlue = 0
        specRed = 0
        specGreen = 0
        specBlue = 0
        for l in lightList:
            # cast shadows
            lightRay = create_ray(l.pos, PVector.sub(nearestHit.pos, l.pos))
            if nearestHit.type == "s":
                lightHit = intersect_sphere(lightRay)
            else:
                lightHit = intersect_triangle(lightRay)
            
            visible = 1
            if lightHit.id != nearestHit.id:
                visible = 0
            
            # light color
            Lr = l.col.x
            Lg = l.col.y
            Lb = l.col.z
            
            # light position
            L = PVector(l.pos.x - nearestHit.pos.x, l.pos.y - nearestHit.pos.y, l.pos.z - nearestHit.pos.z)
            L.normalize()
            
            # diffuse shading
            lightRed += (Lr * max(0, (N.dot(L))))*visible
            lightGreen += (Lg * max(0, (N.dot(L))))*visible
            lightBlue += (Lb * max(0, (N.dot(L))))*visible
            
            #Phong
            # calculate R
            Rr = 2*N.x * (N.dot(L)) - L.x
            Rg = 2*N.y * (N.dot(L)) - L.y
            Rb = 2*N.z * (N.dot(L)) - L.z
            R = PVector(Rr, Rg, Rb)
            R.normalize()
            
            # calculate E
            E = PVector(eyeRay.orig.x-nearestHit.pos.x, eyeRay.orig.y-nearestHit.pos.y, eyeRay.orig.z-nearestHit.pos.z)
            E.normalize()
            
            # Blinn-Phong
            # calculate H
            H = PVector.add(E, L)
            H.normalize()
            
            # specular shading - Blinn-Phong
            # specRed += (Lr * (H.dot(N))**P)*visible
            # specGreen += (Lg * (H.dot(N))**P)*visible
            # specBlue += (Lb * (H.dot(N))**P)*visible
            
            # specular shading - Phong
            specRed += visible * Lr * max(0, R.dot(E))**P
            specGreen += visible * Lg * max(0, R.dot(E))**P
            specBlue += visible * Lb * max(0, R.dot(E))**P
        
        # reflections
        crefl = 0
        if surface.krefl != 0:
            # calculate reflection ray
            # d = PVector.sub(nearestHit.pos, eyeRay.orig)
            d = PVector.sub(eyeRay.orig, nearestHit.pos)
            # d = eyeRay.orig
            # d = eyeRay.dir
            # d.normalize()
            # reflDir = PVector.sub(d, PVector.mult(N, 2*(d.dot(N))))
            reflDir = PVector.sub(PVector.mult(N, 2*(PVector.dot(d, N))), d)
            # reflDir.normalize()
            # offset = PVector.mult(N, 0.000001)
            offset = PVector.mult(reflDir, 0.000001)
            reflOrig = PVector.add(nearestHit.pos, offset)
            # reflOrig.normalize()
            # reflOrig = nearestHit.pos
            refl = create_ray(reflOrig, reflDir)
            
            #generate a new nearestHit using refl?
            sphereHit = intersect_sphere(refl)
            # triHit = intersect_triangle(refl)
            # FIX
            nearestHit = sphereHit
            # if nearestHit.id == 3:
            #     print(nearestHit.id)
            rec += 1
            crefl = shading(nearestHit, eyeRay, rec)
        
        # Calculate final color values
        Cr = (Dr * ( lightRed)) + Sr*specRed + Ar + surface.krefl * red(crefl)
        Cg = (Dg * ( lightGreen)) + Sg*specGreen + Ag + surface.krefl * green(crefl)
        Cb = (Db * ( lightBlue)) + Sb*specBlue + Ab + surface.krefl * blue(crefl)
        
        pix_color = color(Cr, Cg, Cb)
        return pix_color
    else:
        pc = color(scene.bg.x, scene.bg.y, scene.bg.z)
        return pc
    
# calculate intersection with triangle
def intersect_triangle(ray):
    
    nearestHit = create_hit(-1, None, 0, None, "")
    for tri in triangles:
        # CRAMER'S RULE
        xa, ya, za = tri.v1.x, tri.v1.y, tri.v1.z
        xb, yb, zb = tri.v2.x, tri.v2.y, tri.v2.z
        xc, yc, zc = tri.v3.x, tri.v3.y, tri.v3.z
        xd, yd, zd = ray.dir.x, ray.dir.y, ray.dir.z
        xe, ye, ze = ray.orig.x, ray.orig.y, ray.orig.z
        
        # find normal
        v1 = tri.v1
        v2 = tri.v2
        v3 = tri.v3
        E1 = PVector ( v2.x-v1.x, v2.y-v1.y, v2.z-v1.z )
        E2 = PVector ( v3.x-v1.x, v3.y-v1.y, v3.z-v1.z )
        N = E1.cross(E2)
        N.normalize()
        N = N.mult(-1)
        
        dx = ray.dir.x
        dy = ray.dir.y
        dz = ray.dir.z
        x0 = ray.orig.x
        y0 = ray.orig.y
        z0 = ray.orig.z
        
        a = xa - xb
        b = ya - yb
        c = za - zb
        d = xa - xc
        e = ya - yc
        f = za - zc
        g = xd
        h = yd
        i = zd
        j = xa - xe
        k = ya - ye
        l = za - ze
        
        m = float(a*(e*i - h*f) + b*(g*f - d*i) + c*(d*h - e*g))
        if m == 0:
            continue
        beta = (j*(e*i - h*f) + k*(g*f - d*i) + l*(d*h - e*g)) / float(m)
        gamma = (i*(a*k - j*b) + h*(j*c - a*l) + g*(b*l - k*c)) / float(m)
        t = -( f*(a*k - j*b) + e*(j*c - a*l) + d*(b*l - k*c) ) / float(m)
        
        if t < 0:
            continue
        if gamma < 0 or gamma > 1:
            continue
        if beta < 0 or beta > 1 - gamma:
            continue
        
        # calculate position of intersection
        xpos = x0 + t*(dx - x0)
        ypos = y0 + t*(dy - y0)
        zpos = z0 + t*(dz - z0)
        intersection = PVector(xpos, ypos, zpos)
        
        hit = create_hit(t, intersection, tri.id, N, "t")
        if hit.t >= 0 and hit.t < nearestHit:
            nearestHit = hit
        
        # IN-CLASS METHOD
        # find normal
        # v1 = tri.v1
        # v2 = tri.v2
        # v3 = tri.v3
        # E1 = PVector ( v2.x-v1.x, v2.y-v1.y, v2.z-v1.z )
        # E2 = PVector ( v3.x-v1.x, v3.y-v1.y, v3.z-v1.z )
        # N = E1.cross(E2)
        # N.normalize()
        
        # N = N.mult(-1)
        
        # # prepare for calculations
        # a = N.x
        # b = N.y
        # c = N.z
        # px0 = v1.x
        # py0 = v1.y
        # pz0 = v1.z
        # d = -a*px0 - b*py0 - c*pz0
        
        # dx = ray.dir.x
        # dy = ray.dir.y
        # dz = ray.dir.z
        # x0 = ray.orig.x
        # y0 = ray.orig.y
        # z0 = ray.orig.z
        
        # # find t
        # if (a*dx + b*dy + c*dz) == 0:    # then ray does not intersect plane at all
        #     t = -1
        #     continue
        # else:
        #     t = -(a*x0 + b*y0 + c*z0 + d) / (a*dx + b*dy + c*dz)
        
        # # calculate position of intersection
        # xpos = x0 + t*(dx - x0)
        # ypos = y0 + t*(dy - y0)
        # zpos = z0 + t*(dz - z0)
        # intersection = PVector(xpos, ypos, zpos)
        
        # # project polygon to 2D
        # # for each vertex in tri
        # vertices = [tri.v1, tri.v2, tri.v3]
        # right = max(tri.v1.x, tri.v2.x, tri.v3.x)
        # left = min(tri.v1.x, tri.v2.x, tri.v3.x)
        # top = max(tri.v1.y, tri.v2.y, tri.v3.y)
        # bottom = min(tri.v1.y, tri.v2.y, tri.v3.y)
        # near = max(tri.v1.y, tri.v2.y, tri.v3.y)
        # far = min(tri.v1.y, tri.v2.y, tri.v3.y)
        
        # right = 5
        # left = -5
        # top = 5
        # bottom = -5
        # near = 5
        # far = -5
        
        # xypoints = []
        # for v in vertices:
        #     # project to xy-plane
        #     x = v.x
        #     y = v.y
        #     newX = (width/(right-left)) * (x - left)
        #     newY = (height/(top-bottom)) * (y-bottom)
        #     newV = PVector(newX, newY)
        #     xypoints.append(newV)
        # xyp1 = xypoints[0]
        # xyp2 = xypoints[1]
        # xyp3 = xypoints[2]
        # xyarea = xyp1.x*xyp2.y + xyp2.x*xyp3.y + xyp3.x*xyp1.y - xyp1.x*xyp3.y - xyp2.x*xyp1.y - xyp3.x*xyp2.y
            
        # # project to yz-plane
        # # TODO
            
        # # project to xz-plane
        # # TODO
        
        # # figure out which projection will give you the largest area
        # # project intersection to 2D using above projection plane
        # # if xyarea is largest
        # qx = (width/(right-left)) * (xpos-left)    # intersection
        # qy = (height/(top-bottom)) * (ypos-bottom)
        # area = xyarea
        # p1 = xyp1
        # p2 = xyp2
        # p3 = xyp3
        # # if yzarea is largest
        
        # # if xzarea is largest
        
        # inside = 0
        # # Half-plane test
        # V = PVector.sub(p2, p1)
        # V.normalize()
        # a = -V.y
        # b = V.x
        # c = -(a*p1.x) -(b*p1.y)
        # Qresult = a*qx + b*qy + c
        # P3result = a*p3.x + b*p3.y + c
        # if Qresult > 0 and P3result > 0:
        #     inside += 1
        # elif Qresult < 0 and P3result < 0:
        #     inside += 1
        # else:
        #     continue
        
        # hit = create_hit(t, intersection, tri.id, N, "t")
        # if hit.t >= 0 and hit.t < nearestHit:
        #     nearestHit = hit
            
    return nearestHit

# calculate intersection with sphere
def intersect_sphere(ray):
    nearestHit = create_hit(-1, None, 0, None, "")
    for s in spheres:
        x0 = ray.orig.x
        y0 = ray.orig.y
        z0 = ray.orig.z
        xc = s.center.x
        yc = s.center.y
        zc = s.center.z
        dx = ray.dir.x
        dy = ray.dir.y
        dz = ray.dir.z
        r = s.radius
        id = s.id
        
        #calculate t
        a = dx**2 + dy**2 + dz**2
        b = 2*(dx*(x0-xc) + dy*(y0-yc) + dz*(z0-zc))
        c = xc**2 + yc**2 + zc**2 + x0**2 + y0**2 + z0**2 - 2*(xc*x0 + yc*y0 + zc*z0) - r**2
        
        if 2*a == 0:
            t1 = 0
            t2 = 0
        else:
            t1 = (-b+sqrt(b*b - 4*a*c))/(2*a)
            t2 = (-b-sqrt(b*b - 4*a*c))/(2*a)
    
        #Choose the t that is smaller and positive
        t = t1
        if t1 < 0 and t2 >= 0:
            t = t2
        elif t2 < 0 and t1 >= 0:
            t = t1
        elif t1 >= 0 and t2 >= 0 and t1 <= t2:
            t = t1
        elif t1 >= 0 and t2 >= 0 and t2 <= t1:
            t = t2
            
        #calculate the position of the intersection
        xpos = x0 + t*(dx - x0)
        ypos = y0 + t*(dy - y0)
        zpos = z0 + t*(dz - z0)
        intersection = PVector(xpos, ypos, zpos)
        
        #calculate normal
        nx = intersection.x - xc
        ny = intersection.y - yc
        nz = intersection.z - zc
        N = PVector(nx, ny, nz)
        N.normalize()
        
        hit = create_hit(t, intersection, id, N, "s")    
        if hit.t > 0 and hit.t < nearestHit:
            nearestHit = hit
        
    return nearestHit