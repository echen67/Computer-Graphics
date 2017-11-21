// Emily Chen

#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  //gl_FragColor = vec4(diffuse_color.rgb, 1.0);

  float delta = 1.0/200.0;
  vec2 top_coord = vec2(vertTexCoord.x, vertTexCoord.y+delta);
  vec4 top_color = texture2D(texture, top_coord);
  float top_avg = (top_color.r*0.3 + top_color.g*0.6 + top_color.b*0.1) / 3.0;

  vec2 bottom_coord = vec2(vertTexCoord.x, vertTexCoord.y-delta);
  vec4 bottom_color = texture2D(texture, bottom_coord);
  float bottom_avg = (bottom_color.r*0.3 + bottom_color.g*0.6 + bottom_color.b*0.1) / 3.0;

  vec2 right_coord = vec2(vertTexCoord.x+delta, vertTexCoord.y);
  vec4 right_color = texture2D(texture, right_coord);
  float right_avg = (right_color.r*0.3 + right_color.g*0.6 + right_color.b*0.1) / 3.0;

  vec2 left_coord = vec2(vertTexCoord.x-delta, vertTexCoord.y);
  vec4 left_color = texture2D(texture, left_coord);
  float left_avg = (left_color.r*0.3 + left_color.g*0.6 + left_color.b*0.1) / 3.0;

  //float avg = (diffuse_color.r + diffuse_color.g + diffuse_color.b) / 3.0;
  float middle_avg = (diffuse_color.r*0.3 + diffuse_color.g*0.6 + diffuse_color.b*0.1) / 3.0;

  float laplace = top_avg + bottom_avg + right_avg + left_avg - 4*middle_avg;
  laplace = laplace * 10;
  //laplace = laplace * .125;

  gl_FragColor = vec4(laplace, laplace, laplace, 1.0);
  //gl_FragColor = vec4(0,0,0,1);
}

