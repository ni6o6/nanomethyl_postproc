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
run_time = (time.time()-start_time)/60

        
def add_haplotypes(hap_bampath, me_bampath, out_bampath) :
    
    hap1_1_qnames = {}
    hap1_2_qnames = {}
    hap1_3_qnames = {}
    hap1_4_qnames = {}
    hap1_5_qnames = {}
    hap1_6_qnames = {}
    hap1_7_qnames = {}
    hap1_8_qnames = {}
    hap1_9_qnames = {}
    hap1_10_qnames = {}
    hap1_11_qnames = {}
    hap1_12_qnames = {}
    hap1_13_qnames = {}
    hap1_14_qnames = {}
    hap1_15_qnames = {}
    hap1_16_qnames = {}
    hap1_17_qnames = {}
    hap1_18_qnames = {}
    hap1_19_qnames = {}
    hap1_20_qnames = {}
    hap1_21_qnames = {}
    hap1_22_qnames = {}
    hap1_X_qnames = {}
    hap1_Y_qnames = {}
    hap2_1_qnames = {}
    hap2_2_qnames = {}
    hap2_3_qnames = {}
    hap2_4_qnames = {}
    hap2_5_qnames = {}
    hap2_6_qnames = {}
    hap2_7_qnames = {}
    hap2_8_qnames = {}
    hap2_9_qnames = {}
    hap2_10_qnames = {}
    hap2_11_qnames = {}
    hap2_12_qnames = {}
    hap2_13_qnames = {}
    hap2_14_qnames = {}
    hap2_15_qnames = {}
    hap2_16_qnames = {}
    hap2_17_qnames = {}
    hap2_18_qnames = {}
    hap2_19_qnames = {}
    hap2_20_qnames = {}
    hap2_21_qnames = {}
    hap2_22_qnames = {}
    hap2_X_qnames = {}
    hap2_Y_qnames = {}
    
    with pysam.AlignmentFile(hap_bampath,'rb') as hap_bam :
      
        for read in hap_bam:
            tags = read.tags
            taglabels = [ x[0] for x in tags ]
            if "HP" not in taglabels : continue
            qname = read.query_name
            contig = str(read.reference_id)
            contig_n = contig.replace('chr','')
            hap = tags[taglabels.index("HP")][1]
            
            if hap == 1 :
                if contig_n == '1':
                    hap1_1_qnames[qname] = 1
                if contig_n == '2':
                    hap1_2_qnames[qname] = 1
                if contig_n == '3':
                    hap1_3_qnames[qname] = 1
                if contig_n == '4':
                    hap1_4_qnames[qname] = 1
                if contig_n == '5':
                    hap1_5_qnames[qname] = 1
                if contig_n == '6':
                    hap1_6_qnames[qname] = 1
                if contig_n == '7':
                    hap1_7_qnames[qname] = 1
                if contig_n == '8':
                    hap1_8_qnames[qname] = 1
                if contig_n == '9':
                    hap1_9_qnames[qname] = 1
                if contig_n == '10':
                    hap1_10_qnames[qname] = 1
                if contig_n == '11':
                    hap1_11_qnames[qname] = 1
                if contig_n == '12':
                    hap1_12_qnames[qname] = 1
                if contig_n == '13':
                    hap1_13_qnames[qname] = 1                   
                if contig_n == '14':
                    hap1_14_qnames[qname] = 1
                if contig_n == '15':
                    hap1_15_qnames[qname] = 1
                if contig_n == '16':
                    hap1_16_qnames[qname] = 1
                if contig_n == '17':
                    hap1_17_qnames[qname] = 1
                if contig_n == '18':
                    hap1_18_qnames[qname] = 1
                if contig_n == '19':
                    hap1_19_qnames[qname] = 1
                if contig_n == '20':
                    hap1_20_qnames[qname] = 1                    
                if contig_n == '21':
                    hap1_21_qnames[qname] = 1
                if contig_n == '22':
                    hap1_22_qnames[qname] = 1
                if contig_n == 'X':
                    hap1_X_qnames[qname] = 1
                if contig_n == 'Y':
                    hap1_Y_qnames[qname] = 1                      
            elif hap == 2 :
                if contig_n == '1':
                    hap2_1_qnames[qname] = 2
                if contig_n == '2':
                    hap2_2_qnames[qname] = 2
                if contig_n == '3':
                    hap2_3_qnames[qname] = 2
                if contig_n == '4':
                    hap2_4_qnames[qname] = 2
                if contig_n == '5':
                    hap2_5_qnames[qname] = 2
                if contig_n == '6':
                    hap2_6_qnames[qname] = 2
                if contig_n == '7':
                    hap2_7_qnames[qname] = 2
                if contig_n == '8':
                    hap2_8_qnames[qname] = 2
                if contig_n == '9':
                    hap2_9_qnames[qname] = 2
                if contig_n == '10':
                    hap2_10_qnames[qname] = 2
                if contig_n == '11':
                    hap2_11_qnames[qname] = 2
                if contig_n == '12':
                    hap2_12_qnames[qname] = 2
                if contig_n == '13':
                    hap2_13_qnames[qname] = 2                   
                if contig_n == '14':
                    hap2_14_qnames[qname] = 2
                if contig_n == '15':
                    hap2_15_qnames[qname] = 2
                if contig_n == '16':
                    hap2_16_qnames[qname] = 2
                if contig_n == '17':
                    hap2_17_qnames[qname] = 2
                if contig_n == '18':
                    hap2_18_qnames[qname] = 2
                if contig_n == '19':
                    hap2_19_qnames[qname] = 2
                if contig_n == '20':
                    hap2_20_qnames[qname] = 2                   
                if contig_n == '21':
                    hap2_21_qnames[qname] = 2
                if contig_n == '22':
                    hap2_22_qnames[qname] = 2
                if contig_n == 'X':
                    hap2_X_qnames[qname] = 2 
                if contig_n == 'Y':
                    hap2_Y_qnames[qname] = 2      

    with pysam.AlignmentFile(me_bampath,'rb') as me_bam:
        f = pysam.AlignmentFile(out_bampath, 'wb',template = me_bam)
        for m_read in me_bam:
            me_contig = str(m_read.reference_id)
            me_contig_n = me_contig.replace('chr','')
            if me_contig_n == '1':
                if m_read.query_name in hap1_1_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_1_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '2':
                if m_read.query_name in hap1_2_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_2_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '3':
                if m_read.query_name in hap1_3_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_3_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '4':
                if m_read.query_name in hap1_4_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_4_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '5':
                if m_read.query_name in hap1_5_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_5_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '6':
                if m_read.query_name in hap1_6_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_6_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '7':
                if m_read.query_name in hap1_7_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_7_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '8':
                if m_read.query_name in hap1_8_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_8_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '9':
                if m_read.query_name in hap1_9_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_9_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '10':
                if m_read.query_name in hap1_10_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_10_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '11':
                if m_read.query_name in hap1_11_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_11_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '12':
                if m_read.query_name in hap1_12_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_12_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '13':
                if m_read.query_name in hap1_13_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_13_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '14':
                if m_read.query_name in hap1_14_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_14_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '15':
                if m_read.query_name in hap1_15_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_15_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '16':
                if m_read.query_name in hap1_16_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_16_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '17':
                if m_read.query_name in hap1_17_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_17_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '18':
                if m_read.query_name in hap1_18_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_18_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '19':
                if m_read.query_name in hap1_19_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_19_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '20':
                if m_read.query_name in hap1_20_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_20_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '21':
                if m_read.query_name in hap1_21_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_21_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == '22':
                if m_read.query_name in hap1_22_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_22_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == 'X':
                if m_read.query_name in hap1_X_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_X_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)
            if me_contig_n == 'Y':
                if m_read.query_name in hap1_Y_qnames:
                    m_read.set_tags([('HP', 1, 'i')])
                    f.write(m_read)
                elif m_read.query_name in hap2_Y_qnames:
                    m_read.set_tags([('HP', 2, 'i')])
                    f.write(m_read)
                else:
                    f.write(m_read)    
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

'''
hap_bampath = '../whatshap/COLO829_phased2.chr21.bam'
me_bampath = 'COLO829_chr21_me_refbase.bam'
out_bampath = 'COLO829_chr21_me_hap_test3.bam'
'''