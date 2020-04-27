from src.webcamList import webcams
from src.dataCollector.frameCaptureWrapper import frameCaptureWrapper
from src.dataCollector.screenshotCaptureWrapper import screenshotCaptureWrapper
from src.utils.times import tz_finder
from src.utils import dataUtils, emailNotification
from datetime import datetime 
import pytz

 
img_prefix = dataUtils.image_prefix_generator('dublin')
# num_im = int(input("Enter the number of images:"))
# time_interval = int(input("Enter the time interval (in min):"))
# time_interval = time_interval * 60
num_im = 2
time_interval = 30
# print(time_interval)
city = 'Dublin'
webcam = webcams.dublin
tz = tz_finder(city)
start = datetime.now(pytz.timezone(tz))
bystreamflag = True

if bystreamflag:
    try:
        collector = frameCaptureWrapper(webcam_url=webcam, city=city, image_prefix=img_prefix)
        res = collector.capture_frame_by_stream_wrapper(num_im=num_im, time_interval=time_interval)
        method = 'stream'

    except:
        collector = screenshotCaptureWrapper(webcam_url=webcam, city=city, image_prefix=img_prefix)
        res = collector.capture_frame_by_screenshot_wrapper(num_im=num_im, time_interval=time_interval)
        method = 'screenshot'
else:
    collector = screenshotCaptureWrapper(webcam_url=webcam, city=city, image_prefix=img_prefix)
    res = collector.capture_frame_by_screenshot_wrapper(num_im=num_im, time_interval=time_interval)
    method = 'screenshot'
end = datetime.now(pytz.timezone(tz))
dataUtils.store_as_csv(data=res, target_img_path=collector.target_img_path, image_prefix=img_prefix, method=method)
emailNotification.emailNotification(prefix=img_prefix, num=num_im, time_interval=time_interval, start=start, end=end, url=webcam, method=method)
