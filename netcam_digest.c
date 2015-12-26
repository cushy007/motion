/*
 *    netcam_digest.c
 *
 *    Module for handling webcams with digest HTTP authentication.
 *
 *    Copyright 2015, Johann Saunier
 *    This program is published under the GNU Public license
 */

#include "rotate.h"    /* already includes motion.h */


extern int http_digest(const char *header)
{
	return 7;
}
