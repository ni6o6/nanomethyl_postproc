#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:50:22 2020

@author: naokoiida

infile: .methylation_frequency.tsv 
chromosome[0] 
start 
end 
num_motifs_in_group 
called_sites[4] 
called_sites_methylated 
freq 
group_sequence[7]
"""

from argparse import ArgumentParser
import pandas as pd 
import matplotlib.pyplot as plt
import pathlib

def methyl1base(input_file, output_file, r):
    
    fpath = pathlib.Path(output_file)
    fstem = fpath.stem
    bed_file = fstem+".bedGraph"  
    
    pf = pd.read_csv(input_file, sep="\t", header=0) 
    print(pf['called_sites'].describe())
    print(pf['methylated_frequency'].describe())
    
    plt.plot(figsize=(3, 3))
    plt.hist(pf['called_sites'], bins=100, range=(0, 100))
    plt.title(f'{fstem} depth (0-100)')
    plt.xlabel('called sites')
    plt.ylabel('count')
    #plt.show()
    plt.savefig(f'Hist_{fstem}_depth.png', dpi=75 * 1.5 )
    plt.close()
  
    
    with open(input_file, 'r') as hin, open(output_file, 'w') as hout, open(bed_file, 'w') as jout:
        
        for line in hin:
            F = line.rstrip('\n').split('\t')
            if F[0]=='chromosome':
                hout.write('chromosome\tstart\tend\tcalled_sites\tcalled_sites_methylated\tmethylated_frequency\n')
                continue
            motif_num = 0
            seq = F[7]
            pos_start = int(F[1])
            depth = int(F[4])
            
            if depth >= r:
                for i in range(0,len(seq)-1):
                    if seq[i]+seq[i+1] == 'CG':
                        if motif_num == 0:
                            C1st = i
                        
                        pos = pos_start+i-C1st
                        
                        #position is 0-coordinate
                        rec = '\t'.join([str(F[0]),str(pos),str(pos+1),str(F[4]),str(F[5]),str(F[6])])+'\n'
                        hout.write(rec)
                        bed = '\t'.join([str(F[0]),str(pos),str(pos+1),str(F[6])])+'\n'
                        jout.write(bed)
                        motif_num = motif_num+1

    pf2 = pd.read_csv(output_file, sep="\t", header=0)
    #pf[["called_sites"]].max(axis=0)  
    print(pf2['called_sites'].describe())
    print(pf2['methylated_frequency'].describe())
    plt.plot(figsize=(3, 3))
    plt.hist(pf2['methylated_frequency'], bins=100)
    plt.title(f'{fstem} depth>={r}')
    plt.xlabel('methylated_frequency')
    plt.ylabel('count')
    #plt.show()
    plt.savefig(f'Hist_{fstem}.png', dpi= 75 * 1.5 )
    plt.close()


if __name__ == "__main__":
	
    # Parameters to be input.
    parser = ArgumentParser()
    parser.add_argument("-input_file", action="store", dest="infile", help="input tsv file", required=True)
    parser.add_argument("-output_file", action="store", dest="outfile", help="output file", required=True)
    parser.add_argument("-r", action="store", dest="r", help="read depth >= r", required=True, default=10)
    o = parser.parse_args()
    
    infile = o.infile
    outfile = o.outfile
    r = o.r
    
    filter(infile, outfile, r)
    
input_file = 'COLO829.methylation_frequency.tsv'
output_file = 'COLO829.methylation_frequency.1b.fil10.tsv'
r = 10