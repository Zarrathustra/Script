#!/usr/bin/env python
import os,sys
from metadata import *
import random
import math
import multiprocessing

from optparse import OptionParser
prog_name=os.path.basename(sys.argv[0])
usage="""
{prog} < --input_data_star data.star> < --input_sampling_star sampling.star  > < -o output star file >  [--reverse]
""".format(prog=prog_name)
optParser= OptionParser(usage)
#optParser.add_option("-i","--input_opti_star",action="store",type="str",dest="input_opti_star",default="",help="Input relion optimiser.star file. [default: %default]")
optParser.add_option("--input_data_star",action="store",type="str",dest="input_data_star",default="",help="Input relion data.star file. [default: %default]")
optParser.add_option("--input_sampling_star",action="store",type="str",dest="input_sampling_star",default="",help="Input relion sampling.star file. [default: %default]")
optParser.add_option("-o","--outputstar",action="store",type="str",dest="outputstar",default="",help="Output relion data.star file. [default: %default]")
optParser.add_option("-b","--outputbild",action="store",type="str",dest="outputbild",default="",help="Output angular distribution .bild file. [default: %default]")
optParser.add_option("--upper_limit",action="store",type="float",dest="upper_limit",default=3.0,help="The upper limit of particles per direction to be perserved in times of average particles number per directions. Specify -1 to disable this option. [default: %default]")
#optParser.add_option("--reverse",action="store_true",dest="reverse",default=False,help="To sort reservely . [default: %default]")
optParser.add_option("--multicpu",action="store",type="int",dest="multicpu",default=0,help="Number of cpu used for parallel processing. [default: %default]",metavar="24")
(options,args)=optParser.parse_args()

if not options.input_data_star or not options.input_sampling_star:
	print "Please specify a data.star file and a sampling.star file."
	exit()
if not options.outputstar:
	ps=options.input_data_star.rfind(".")
	if ps >= 0 :
		options.outputstar = options.input_data_star[:ps] + "_balanced.star"
	else:
		options.outputstar = options.input_data_star + "_balanced.star"
if not options.outputbild:
	ps=options.input_data_star.rfind(".")
	if ps >= 0 :
		options.outputbild = options.input_data_star[:ps] + "_balanced.bild"
	else:
		options.outputbild = options.input_data_star + "_balanced.bild"


# Find the index of minimum distance
def i_min_distance_samdir(rot_tilt):
	min_dist = 1000000.
	min_samdir = -1
	i_samdir=0
	for samdir in rot_tilt[2]:
		ang_dist = (rot_tilt[0] - samdir[0]) ** 2 + (rot_tilt[1] - samdir[1]) ** 2
		if ang_dist <  min_dist :
			min_dist = ang_dist
			min_samdir = i_samdir
		i_samdir += 1
	return min_samdir

class EulerAngleBalancer(object):
	def __init__(self,options):
		super(EulerAngleBalancer,self).__init__()
		self.options=options
	def read(self,fn_data,fn_sampling):
		self.sampling=sampling_meta(fn_sampling)
		self.data=data_meta(fn_data)
	def __call__(self):
		self.run()
	def run(self):
		self.read(self.options.input_data_star,self.options.input_sampling_star)
		self.classifier()
		self.filter()
		self.write()
		self.write_bild()
	def classifier(self):
		# iangrot,iangtilt,iangpsi are integer
		try:
			iangrot=self.data.data_images["labels"]["_rlnAngleRot"] - 1
			iangtilt=self.data.data_images["labels"]["_rlnAngleTilt"] - 1
		except:
			iangrot=self.data.data_["labels"]["_rlnAngleRot"] - 1
			iangtilt=self.data.data_["labels"]["_rlnAngleTilt"] - 1
		iangrot_sampling=self.sampling.data_sampling_directions["labels"]["_rlnAngleRot"] - 1 
		iangtilt_sampling=self.sampling.data_sampling_directions["labels"]["_rlnAngleTilt"] - 1 
		# Initialise self.records_samdir
		self.nr_samdirs=len(self.sampling.data_sampling_directions["datas"])
		try:
			self.nr_records = len(self.data.data_images["datas"])
		except:
			self.nr_records = len(self.data.data_["datas"])
		# records per sampling direction
		self.records_samdir=[]
		for i_samdir in range(self.nr_samdirs):
			self.records_samdir.append([])
		self.samdirs = [ [float(e[iangrot_sampling]),float(e[iangtilt_sampling])] for e in self.sampling.data_sampling_directions["datas"]]
		try:
			rots_tilts =[ [float(record[iangrot]),float(record[iangtilt]),self.samdirs] for record in self.data.data_images["datas"]]
		except:
			rots_tilts =[ [float(record[iangrot]),float(record[iangtilt]),self.samdirs] for record in self.data.data_["datas"]]
		if not self.options.multicpu:
			self.options.multicpu = multiprocessing.cpu_count()
		pool=multiprocessing.Pool(self.options.multicpu)
		indexes_min_samdir = pool.map(i_min_distance_samdir,rots_tilts)
		pool.close()
		pool.join()
		indexes=iter(indexes_min_samdir)
		try:
			for record in self.data.data_images["datas"]:
				self.records_samdir[indexes.next()].append(record)
		except:
			for record in self.data.data_["datas"]:
				self.records_samdir[indexes.next()].append(record)
	def filter(self):
		nr_significant_samdir = 0
		for records in self.records_samdir:
			if len(records) > 0:
				nr_significant_samdir += 1
		self.nr_significant_samdir = nr_significant_samdir
		# average number records per direction
		nr_avg_records_per_dir = self.nr_records  // self.nr_significant_samdir
		upper_limit_records_per_dir = int( nr_avg_records_per_dir * self.options.upper_limit )
		for i_samdir in range(self.nr_samdirs):
			if  upper_limit_records_per_dir > 0 and  len(self.records_samdir[i_samdir]) >  upper_limit_records_per_dir:
				try:
					i_LLC=self.data.data_images["labels"]["_rlnLogLikeliContribution"]
				except:
					i_LLC=self.data.data_["labels"]["_rlnLogLikeliContribution"]
				self.records_samdir[i_samdir]=sorted(self.records_samdir[i_samdir],key=lambda e:float(e[i_LLC]),reverse=True)
				#self.records_samdir[i_samdir]=random.sample(self.records_samdir[i_samdir],nr_avg_records_per_dir * 2)
				self.records_samdir[i_samdir]=self.records_samdir[i_samdir][:upper_limit_records_per_dir]
	def write(self):
		f=open(self.options.outputstar,"w")
		f.write("\n")
		f.write("data_images\n")
		f.write("\n")
		f.write("loop_\n")
		try:
			sorted_labels=sorted(self.data.data_images["labels"].items(),key=lambda e:e[1],reverse=False)
		except:
			sorted_labels=sorted(self.data.data_["labels"].items(),key=lambda e:e[1],reverse=False)
		# Output _rlnLabel
		for label in sorted_labels :
			f.write("%s\t#%d\n"%(label[0],label[1]))
		# Output data records
		for records in self.records_samdir:
			for record in records:
				f.write(" ".join(record) + "\n")
		f.close()

	def write_bild(self,R=100.,width_frac = 0.5 , Rmax_frac=0.1,):
		f=open(self.options.outputbild,"w")
		psistep = float(self.sampling.data_sampling_general["labels"]["_rlnPsiStep"])
		width = width_frac * math.pi * R * psistep / 360.
		pdfs = [ float(len(records))  for records in self.records_samdir ]
		pdfmean = sum(pdfs) / len(pdfs)
		pdfmax=max(pdfs)
		pdfsigma = ( sum([ (pdf - pdfmean) ** 2  for pdf in pdfs]) / len(pdfs) ) ** 0.5
		n=0
		for pdf in pdfs:
			if pdf > 0.1:
				color = (pdf - pdfmean) / pdfsigma
				color = min(color,5.)
				color = max(color,-1.)
				color /= 6.
				color += 1./6.
				phi,theta=self.samdirs[n][0]/180.*math.pi,self.samdirs[n][1]/180.*math.pi
				Rp = R + Rmax_frac * R * pdf / pdfmax
				f.write(".color %f 0 %f\n"%(color,1-color))
				f.write(".cylinder %f %f %f %f %f %f %f\n"%(R * math.sin(theta) * math.cos(phi), R * math.sin(theta) * math.sin(phi), R* math.cos(theta),Rp * math.sin(theta) * math.cos(phi), Rp * math.sin(theta) * math.sin(phi), Rp* math.cos(theta), width))
			n += 1
		f.close()

angleBalancer=EulerAngleBalancer(options)
angleBalancer.run()
