from flask import Flask, request, send_file
from rotation import rotate_image
from zoom_in import zoom_center
from warmth import warmth_img
from vignette import vignette_img
from highlight import highlight_correction
from shadows import shadows_img
from sharpen import sharpen_img
from blur import blur_img
from black_white import black_white_img
from brightness import brightness_img
from contrast import contrast_img
from flask_cors import CORS, cross_origin
import cv2
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

img = cv2.imread("./images/image.jpg")

@app.route("/rotation_filter", methods=['POST'])
@cross_origin()
def rotation_filter():
    os.remove("./images/rotation/output.jpg")
    angle = request.get_json()
    output_img = rotate_image(img, angle)
    image_path = './images/rotation/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/zoom_in_filter", methods=['POST'])
@cross_origin()
def zoom_in_filter():
    os.remove("./images/zoom_in/output.jpg")
    zoom_factor = request.get_json()
    output_img = zoom_center(img, zoom_factor)
    image_path = './images/zoom_in/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/warmth_filter", methods=['POST'])
@cross_origin()
def warmth_filter():
    os.remove("./images/warmth/output.jpg")
    r_value = request.form.get('r_value', type=int)
    g_value = request.form.get('g_value', type=int) 
    b_value = request.form.get('b_value', type=int) 
    output_img = warmth_img(img, r_value, g_value, b_value)
    image_path = './images/warmth/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')


@app.route("/vignette_filter", methods=['POST'])
@cross_origin()
def vignette_filter():
    os.remove("./images/vignette/output.jpg")
    value = request.get_json() 
    output_img = vignette_img(img, value)
    image_path = './images/vignette/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')


@app.route("/highlight_filter", methods=['POST'])
@cross_origin()
def highlight_filter():
    os.remove("./images/highlight/output.jpg")
    r_value = request.form.get('r_value', type=int)
    g_value = request.form.get('g_value', type=int) 
    b_value = request.form.get('b_value', type=int)  
    output_img = highlight_correction(img, r_value, g_value, b_value)
    image_path = './images/highlight/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')


@app.route("/shadows_filter", methods=['POST'])
@cross_origin()
def shadows_filter():
    os.remove("./images/shadows/output.jpg")
    r_value = request.form.get('r_value', type=int)
    g_value = request.form.get('g_value', type=int) 
    b_value = request.form.get('b_value', type=int)  
    output_img = shadows_img(img, r_value, g_value, b_value)
    image_path = './images/shadows/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/sharpen_filter", methods=['POST'])
@cross_origin()
def sharpen_filter():
    os.remove("./images/sharpen/output.jpg")
    kernel_size_value = request.form.get('kernel_size_value', type=int)
    output_img = sharpen_img(img, kernel_size_value)
    image_path = './images/sharpen/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/blur_filter", methods=['POST'])  
@cross_origin()
def blur_filter():
    os.remove("./images/blur/output.jpg")
    kernel_size_value = request.form.get('kernel_size_value', type=int)
    output_img = blur_img(img, kernel_size_value)
    image_path = './images/blur/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/black_white_filter", methods=['POST'])
@cross_origin()
def black_white_filter():
    os.remove("./images/black&white/output.jpg")
    value = request.get_json() 
    output_img = black_white_img(img, value)
    image_path = './images/black&white/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/brightness_filter", methods=['POST'])
@cross_origin()
def brightness_filter():
    os.remove("./images/brightness/output.jpg")
    r_value = request.form.get('r_value', type=int)
    g_value = request.form.get('g_value', type=int) 
    b_value = request.form.get('b_value', type=int)  
    output_img = brightness_img(img, r_value, g_value, b_value)
    image_path = './images/brightness/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')

@app.route("/contrast_filter", methods=['POST'])
@cross_origin()
def contrast_filter():
    os.remove("./images/contrast/output.jpg")
    r_value = request.form.get('r_value', type=int)
    g_value = request.form.get('g_value', type=int) 
    b_value = request.form.get('b_value', type=int) 
    output_img = contrast_img(img, r_value, g_value, b_value)
    image_path = './images/contrast/output.jpg'
    cv2.imwrite(image_path, output_img)
    return send_file(image_path, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

