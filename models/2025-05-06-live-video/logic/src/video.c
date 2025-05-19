
#include "sgl_types.h"
#include "sgl.h"
#include "sglConstants.h"
#include "videofunc_mem.h"
#include <cv.h>
#include <highgui.h>

void videofunc_reset(videofunc_mem *mem)
{
	 mem->init = 1; //We are at first cycle !
	 cvReleaseCapture(&(mem->g_Capture));

}

void videofunc(SGLint32 textureID, SGLbool webcam, SGLuint8 videoPath[255UL], SGLbool *isCaptured, SGLfloat *width, SGLfloat *height, videofunc_mem *mem)
{
	if (mem->init) {
		mem->init = 0;
		if (webcam)
		{
			mem->g_Capture  = cvCreateCameraCapture(0);  // webcam
			*width = 640.0;
			*height = 480.0;
		}
		else
		{
			mem->g_Capture = cvCreateFileCapture(videoPath);
			*width = cvGetCaptureProperty( mem->g_Capture, CV_CAP_PROP_FRAME_WIDTH );
			*height = cvGetCaptureProperty( mem->g_Capture, CV_CAP_PROP_FRAME_HEIGHT );
		}
		if (!mem->g_Capture)
		{
			*isCaptured = 0;
		}
	} else {
		IplImage *image = cvQueryFrame(mem->g_Capture);

		if (image)
		{
			//Flip the requested frame
			cvFlip(image, NULL, 0);

			// Convert to RGB
			cvCvtColor(image, image, CV_BGR2RGB);

			// Create Texture
			sglTexImage2Dubv(textureID, SGL_BITMAP_RGB_NOT_TRANSPARENT,
				image->width, image->height, (SGLbyte *) image->imageData, SGL_REPEAT);

			*isCaptured = 1;
		}
		else
		{

			cvSetCaptureProperty(mem->g_Capture, CV_CAP_PROP_POS_AVI_RATIO , 0); //loop playback
		}
	}

}