#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:44:49 2020

@author: naokoiida

add_bam_haptag.py
"""

from argparse import ArgumentParser
import pysam
import time
start_time = time.time()



def add_haplotypes(hap_bampath, me_bampath, out_bampath) :
    with pysam.AlignmentFile(hap_bampath,'rb') as hap_bam :
        #reads = [x for x in bam_hap.fetch(region=coord)] 
        reads = [x for x in hap_bam.fetch()] 
    hap1_qnames = list()
    hap2_qnames = list()
    for read in reads :
        tags = read.tags
        taglabels = [ x[0] for x in tags ]
        if "HP" not in taglabels : continue
        qname = read.query_name 
        hap = tags[taglabels.index("HP")][1]
        if hap == 1 :
            hap1_qnames.append(qname)
        elif hap == 2 :
            hap2_qnames.append(qname)
                      

    with pysam.AlignmentFile(me_bampath,'rb') as me_bam:
        f = pysam.AlignmentFile(out_bampath, 'wb',template = me_bam)
        for read in me_bam:
            #print(read.query_name)
            if read.query_name in hap1_qnames:
                read.set_tags([('HP', 1, 'i')])
                f.write(read)
            elif read.query_name in hap2_qnames:
                read.set_tags([('HP', 2, 'i')])
                
                f.write(read)
    
    f.close()
    
    pysam.index(out_bampath)

if __name__ == "__main__":	
    # Parameters to be input.
    parser = ArgumentParser()
    parser.add_argument("--hap", action="store", dest="hap", help="bam of haplotype call", required=True)
    parser.add_argument("--me", action="store", dest="me", help="bam of methylation call", required=True)
    parser.add_argument("--out", action="store", dest="out", help="output bam name", required=True)
    o = parser.parse_args()
    
    hap_bampath = o.hap
    me_bampath = o.me
    out_bampath = o.out
    
    add_haplotypes(hap_bampath, me_bampath, out_bampath)

hap_bampath = '../whatshap/COLO829_phased2.chr21.bam'
me_bampath = 'COLO829_chr21_me_refbase.bam'
out_bampath = 'COLO829_chr21_me_hap.bam'