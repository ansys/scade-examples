#ifndef VIDEOFUNC_MEM_H
#define VIDEOFUNC_MEM_H

#include <cv.h>
#include <highgui.h>

typedef struct videofunc_mem {
    SGLbool init; //Initialisation flag, true only at first cycle
    CvCapture* g_Capture;
 } videofunc_mem;



#endif