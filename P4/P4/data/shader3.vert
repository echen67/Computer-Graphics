// Emily Chen

#define PROCESSING_TEXTURE_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);

  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  float avg = (diffuse_color.x*0.3 + diffuse_color.y*0.6 + diffuse_color.z*0.1) / 3.0;

  vec4 pos = position;
  pos = vec4(pos.x+avg*normal.x*500, pos.y+avg*normal.y*500, pos.z+avg*normal.z*500, pos.w);
  gl_Position = transform * pos;
}
