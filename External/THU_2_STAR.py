#!/Share/home/yanning/PROGRAM/EMAN2/extlib/bin/python

import os,sys
import random
import math
from EMAN2 import *
from optparse import OptionParser

metalabels="_rlnVoltage \
_rlnDefocusU \
_rlnDefocusV \
_rlnDefocusAngle \
_rlnSphericalAberration \
_rlnAmplitudeContrast \
_rlnPhaseShift \
_rlnImageName \
_rlnMicrographName \
_rlnCoordinateX \
_rlnCoordinateY \
_rlnGroupNumber \
_rlnClassNumber \
_rlnAngleRot \
_rlnAngleTilt \
_rlnAnglePsi \
_rlnOriginX \
_rlnOriginY"

def main():
	prog_name=os.path.basename(sys.argv[0])
	usage="""
	Transform thu file to a metadata file.
	{prog} < -i thu file> < -o output metadata file > 
	""".format(prog=prog_name)
	optParser= OptionParser(usage)
	optParser.add_option("-i",action="store",type="str",dest="input_thu",default="",help="Input thu file. [default: %default]")
	optParser.add_option("-o","--outputstar",action="store",type="str",dest="outputstar",default="",help="Output relion data.star file. [default: %default]")
	(options,args)=optParser.parse_args()
	
	if options.outputstar:
		fout=open(options.outputstar,"w")
		fout.write("\ndata_\n\nloop_\n")
		n=1
		for label in metalabels.split():
			fout.write("%s #%d\n"%(label,n))
			n += 1

		try:
			fin = open(options.input_thu,"r")
		except:
			print "Please input a proper thu file."
			exit()
		t=Transform()
		for line in fin:
			s=line.split()
			# Defocus Angle, Cs, Phase Shift
			s[3]=str(float(s[3]) * 180. / math.pi )
			s[4]=str(float(s[4]) / 10000000. )
			s[6]=str(float(s[6]) * 180. / math.pi )
			t.set_params({"type":"quaternion","e0":float(s[13]),"e1":float(s[14]),"e2":float(s[15]),"e3":float(s[16]),"mirror":0})
			rot=t.get_rotation("spider")
			# Class ID plus 1
			sout=s[:12] + [str(int(s[12]) + 1),str(rot["phi"]),str(rot["theta"]),str(rot["psi"])] + s[17:19]
			fout.write(" ".join(sout) + "\n")
		fin.close()
		fout.close()

if __name__ == "__main__":
	main()
	
	
