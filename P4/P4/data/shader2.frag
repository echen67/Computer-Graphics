// Emily Chen

#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

vec2 multiplyComplex(vec2 a, vec2 b) {
    float real = a.x * b.x - a.y * b.y;
    float imag = a.x * b.y + a.y * b.x;
    vec2 ans = vec2(real, imag);
    return ans;
}

vec2 addComplex(vec2 a, vec2 b) {
    float real = a.x + b.x;
    float imag = a.y + b.y;
    vec2 ans = vec2(real, imag);
    return ans;
}

bool mandelbrot(vec2 c) {
    vec2 z = c;
    vec2 exp = vec2(2, 2);
    for (int i = 0; i < 20; i++) {
        z = addComplex(multiplyComplex(z,z), c);
        if (z.x > 2 || z.y > 2) {
            return false;
        }
    }
    return true;
}

void main() {
    vec2 c = vec2(vertTexCoord.x*3 - 2.1, vertTexCoord.y*3 - 1.5);
    if (c.x >= -2.1 && c.x <= 0.9 && c.y >= -1.5 && c.y <= 1.5) {
        bool ans = mandelbrot(c);
        if (ans) {
            gl_FragColor = vec4(1,1,1,1);
        } else {
            gl_FragColor = vec4(1,0,0,1);
        }
    } else {
        //gl_FragColor = vec4(1.0, vertTexCoord.t, vertTexCoord.t, 1.0);
        gl_FragColor = vec4(1,0,0,1);
    }
}