import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from random import choice
import pytesseract
import numpy as np
import os

from embs import generate_character_dictionary_from_wembs
from utils import save_pickle, load_pickle

# font = ImageFont.truetype("Arial-Bold.ttf",14)

"""
font = ImageFont.truetype("microsoft.ttf", 20)

img = Image.new("RGBA", (500,250),(255,255,255))

draw = ImageDraw.Draw(img)

draw.text((100, 0), "狗", (0,0,0), font=font)

draw = ImageDraw.Draw(img)

img.save("a_test.png")

"""

class synthesizer(object):

    def __init__(self, size, length, font_size, font_dir = 'font'):

        self.font_dir = font_dir

        self.bg_dir = ''

        self.chars = []

        self.size = size

        self.h, self.w = size

        self.colors = []

        self.randoms = dict()

        self.randoms['length'] = list(range(length[0], length[1]))
        
        self.randoms['font_size'] = list(range(font_size[0], font_size[1]))

        self.randoms['w'] = list(range(size[0]))

        self.randoms['h'] = list(range(size[1]))

        self.randoms['rgb'] = list(range(0, 255))

        self.load_font()

    def load_font(self):

        self.randoms['font_family'] = []

        for f in os.listdir(self.font_dir):

            self.randoms['font_family'].append(os.path.join(self.font_dir, f))

    def load_character(self):

        pass

    def load_background(self):

        pass

    def sample(self):

        return boundary

    def sample_random_text(self):

        pass

    def sample_at():

        pass

    def load_character_dictionary(self):

        if not os.path.isfile('dictionary.pkl'):

            d = []

            for wemb in self.wembs:

                d = generate_character_dictionary_from_wembs(d, wemb)

            save_pickle(d, 'dictionary.pkl')

        else:

            d = load_pickle('dictionary.pkl')

        return d

    def random_location(self, font_size):

        x = choice(self.randoms['w'])

        y = choice(self.randoms['h'])

        while x + font_size > self.w or y + font_size > self.h:

            x = choice(self.randoms['w'])

            y = choice(self.randoms['h'])

        return x, y

    def random_color(self):
        
        rgb = [choice(self.randoms['rgb']) for i in range(3)]
        
        return tuple(rgb)

    def synthesize_image(self):

        text = "你是狗"#generate_random_text()

        locations = []

        bboxes = []
        
        img = Image.new("RGBA", (self.h, self.w) ,(255, 255, 255))

        draw = ImageDraw.Draw(img)

        for t in text:

            font_size = choice(self.randoms['font_size'])

            font_family = choice(self.randoms['font_family'])

            bbox = self.find_location(bboxes, font_size)

            font_color = self.random_color()

            frame = np.zeros([self.h, self.w, 3])
            
            font = ImageFont.truetype(font_family, font_size)

            print('font size : ', font_size)

            draw.text((bbox[0], bbox[1]), t, font_color, font = font)

            bboxes.append(bbox)
        
        img.save("a_test.png")

    def find_location(self, bboxes, font_size):

        while True:

            overlapped = False

            x, y = self.random_location(font_size)

            _bbox = [y, x, y + font_size, x + font_size]
            
            for bbox in bboxes:

                if self.IoU(_bbox, bbox) > 0:

                    overlapped = True

                    break
            
            if not overlapped:

                break

        return _bbox

    def check_overlap(self, xy, locations):

        pass

    def IoU(self, candidateBound, groundTruthBound):
        
        cx1 = candidateBound[0]
        cy1 = candidateBound[1]
        cx2 = candidateBound[2]
        cy2 = candidateBound[3]
     
        gx1 = groundTruthBound[0]
        gy1 = groundTruthBound[1]
        gx2 = groundTruthBound[2]
        gy2 = groundTruthBound[3]
     
        carea = (cx2 - cx1) * (cy2 - cy1) #C的面积
        garea = (gx2 - gx1) * (gy2 - gy1) #G的面积
     
        x1 = max(cx1, gx1)
        y1 = max(cy1, gy1)
        x2 = min(cx2, gx2)
        y2 = min(cy2, gy2)
        w = max(0, x2 - x1)
        h = max(0, y2 - y1)
        area = w * h #C∩G的面积
        iou = area / (carea + garea - area)
        return iou

    def get_bbox(self):

        pass

    def draw_bbox(self):

        pass




