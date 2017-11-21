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
    def __init__(self, t, pos, id, n):
        self.t = t        # time, int
        self.pos = pos    # where the ray intersects the object, PVector
        self.id = id      # id of the object that was hit, int
        self.n = n        # normal, PVector

class create_sphere():    
    def __init__(self, radius, center, id, surface):
        self.center = center    # sphere center, PVector
        self.radius = radius    # sphere radius, int
        self.id = id            # position in the spheres list, int
        self.surface = surface  # position of the corresponding surface in the surfaces list, int

def setup():
    size(500, 500) 
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

def interpreter(fname):
    global scene
    scene = create_scene(0, PVector(0,0,0))
    global spheres
    spheres = []
    global lightList
    lightList = []
    global surfaces
    surfaces = []
    global currentSurface
    currentSurface = None
    
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
            aSphere = create_sphere(radius, center, id, currentSurface)
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
            p = words[10]
            krefl = words[11]
            surface = create_surface(diff, amb, spec, p, krefl)
            surfaces.append(surface)
            currentSurface = len(surfaces)-1
        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    orig = PVector(0,0,0)
    global scene
    fov = float(scene.fov)
    k = tan(radians(fov/2))
    global spheres
    global surfaces
    global lightList
    for j in range(height):
        for i in range(width):
            # create an eye ray for pixel (i,j) and cast it into the scene
            newX = i*((2*k)/width) - k
            newY = j*((2*k)/height) - k
            dir = PVector(newX, -newY, -1)
            #dir.normalize()
            eyeRay = create_ray(orig, dir)
            
            #Loop through objects and see if ray intersects with them
            nearestHit = create_hit(-1, None, 0, None)
            for s in spheres:
                newHit = intersect_sphere(eyeRay, s)
                if newHit.t >= 0 and newHit.t < nearestHit:
                    nearestHit = newHit
                
            #Now find the correct color for that pixel
            if nearestHit.t >= 0:
                surfacepos = spheres[nearestHit.id].surface
                surface = surfaces[surfacepos]
                
                N = nearestHit.n
                
                Dr = surface.diff.x
                Dg = surface.diff.y
                Db = surface.diff.z
                
                Ar = surface.amb.x
                Ag = surface.amb.y
                Ab = surface.amb.z
                
                #Summation of all lights
                lightRed = 0
                lightGreen = 0
                lightBlue = 0
                for l in lightList:
                    Lr = l.col.x
                    Lg = l.col.y
                    Lb = l.col.z
                    
                    Lx = l.pos.x - nearestHit.pos.x
                    Ly = l.pos.y - nearestHit.pos.y
                    Lz = l.pos.z - nearestHit.pos.z
                    L = PVector(Lx, Ly, Lz)
                    L.normalize()
                    
                    lightRed += Lr*max(0, (N.dot(L)))
                    lightGreen += Lg*max(0, (N.dot(L)))
                    lightBlue += Lb*max(0, (N.dot(L)))
                
                #Calculate final color values
                Cr = Dr*(Ar + lightRed)
                Cg = Dg*(Ag + lightGreen)
                Cb = Db*(Ab + lightBlue)
                
                pix_color = color(Cr, Cg, Cb)
                set (i, j, pix_color)         # fill the pixel with the calculated color
            else:
                pc = color(scene.bg.x, scene.bg.y, scene.bg.z)
                set (i, j, pc)
    #print("DONE")

# should remain empty for this assignment
def draw():
    pass
    
#calculate intersection with sphere
def intersect_sphere(ray, aSphere):
    x0 = ray.orig.x
    y0 = ray.orig.y
    z0 = ray.orig.z
    xc = aSphere.center.x
    yc = aSphere.center.y
    zc = aSphere.center.z
    dx = ray.dir.x
    dy = ray.dir.y
    dz = ray.dir.z
    r = aSphere.radius
    id = aSphere.id
    
    #calculate t
    a = dx**2 + dy**2 + dz**2
    b = 2*(dx*(x0-xc) + dy*(y0-yc) + dz*(z0-zc))
    c = xc**2 + yc**2 + zc**2 + x0**2 + y0**2 + z0**2 - 2*(xc*x0 + yc*y0 + zc*z0) - r**2
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
    
    hit = create_hit(t, intersection, id, N)
    return hit