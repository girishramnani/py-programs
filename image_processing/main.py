__author__ = 'girish'
import PIL.Image as Image
from PIL.ExifTags import GPSTAGS,TAGS

def ExtractGPSDirectory(filename):

    pilImage=Image.open(filename)
    EXIFData=pilImage._getexif()



    imageTimeStamp="NA"
    CameraModel="NA"
    CameraMake="NA"
    if EXIFData:
        for tag,theValue in EXIFData.items():
            # obtain the tag
            tagValue=TAGS.get(tag,tag)
            # Collect basic image data if available
            if tagValue=='DateTimeOriginal':
                imageTimeStamp=EXIFData.get(tag)
            if tagValue=="Make":
                cameraMake=EXIFData.get(tag)
            if tagValue=='Model':
                cameraModel=EXIFData.get(tag)
            # check the tag for GPS
            if tagValue=="GPSInfo":
            # Found it !
            # Now create a Dictionary to hold the GPS Data
                gpsDictionary={}
            # Loop through the GPS Information
            for curTag in theValue:
                gpsTag=GPSTAGS.get(curTag,curTag)
                gpsDictionary[gpsTag]=theValue[curTag]
                basicEXIFData=[imageTimeStamp,cameraMake,
                cameraModel]
                return gpsDictionary,basicEXIFData
    else:
        return None


def ExtractLatLon(gps):
    # to perform the calculation we need at least
    # lat, lon, latRef and lonRef
    if(gps.has_key("GPSLatitude") and gps.has_key("GPSLongitude") and gps.has_key("GPSLatitudeRef")and gps.has_key("GPSLatitudeRef")):
        latitude =gps["GPSLatitude"]
        latitudeRef =gps["GPSLatitudeRef"]
        longitude =gps["GPSLongitude"]
        longitudeRef=gps["GPSLongitudeRef"]
        lat=ConvertToDegrees(latitude)
        lon=ConvertToDegrees(longitude)
            # If South of the Equator then lat value is negative
        if latitudeRef=="S":
            lat=0-lat
            # Check Longitude Reference
            # If West of the Prime Meridian in
            # Greenwich then the Longitude value is negative
        if longitudeRef=="W":
            lon=0-lon
        gpsCoor={"Lat":lat,"LatRef":latitudeRef,"Lon":lon,"LonRef":longitudeRef}
        return gpsCoor
    else:
        return None

def ConvertToDegrees(gpsCoordinate):
    d0=gpsCoordinate[0][0]
    d1=gpsCoordinate[0][1]
    try:
        degrees=float(d0)/float(d1)
    except:
        degrees=0.0
    m0=gpsCoordinate[1][0]
    m1=gpsCoordinate[1][1]
    try:
        minutes=float(m0)/float(m1)
    except:
        minutes=0.0
    s0=gpsCoordinate[2][0]
    s1=gpsCoordinate[2][1]
    try:
        seconds=float(s0)/float(s1)
    except:
        seconds=0.0
    floatCoordinate=float(degrees+(minutes/60.0)+(seconds/
    3600.0))
    return floatCoordinate
# Check Latitude Reference


x = Image.open("IMG_0179.JPG")

print(x._getexif())
ww = ExtractGPSDirectory("IMG_0179.JPG")
print(ww)