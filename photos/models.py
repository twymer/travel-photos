from django.db import models

# For image data parsing
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def process_exif(self):
        info = Image.open(self.image.file)._getexif()

        ret = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value

        n_sec = ret['GPSInfo'][2][2][0] / float(ret['GPSInfo'][2][2][1])
        n_min = ret['GPSInfo'][2][1][0] / float(ret['GPSInfo'][2][1][1])
        n_deg = ret['GPSInfo'][2][0][0] / float(ret['GPSInfo'][2][0][1])
        w_sec = ret['GPSInfo'][4][2][0] / float(ret['GPSInfo'][4][2][1])
        w_min = ret['GPSInfo'][4][1][0] / float(ret['GPSInfo'][4][1][1])
        w_deg = ret['GPSInfo'][4][0][0] / float(ret['GPSInfo'][4][0][1])

        if ret['GPSInfo'][1] == 'N':
            n_mult = 1
        else:
            n_mult = -1

        # maybe this should be [1]..
        if ret['GPSInfo'][3] == 'E':
            w_mult = 1
        else:
            w_mult = -1

        latitude = n_mult * (n_deg + (n_min + n_sec/60.0)/60.0)
        longitude = w_mult * (w_deg + (w_min + w_sec/60.0)/60.0)

        return { 'latitude': latitude, 'longitude': longitude }

    def save(self, *args, **kwargs):
        image_data = self.process_exif()
        self.latitude = image_data['latitude']
        self.longitude = image_data['longitude']
        super(Photo, self).save(*args, **kwargs)
