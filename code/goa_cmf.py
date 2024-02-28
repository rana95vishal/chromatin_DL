#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:44:35 2024

@author: vishalr
"""

import pandas as pd
import goatools
from goatools import obo_parser
from goatools.anno.genetogo_reader import Gene2GoReader
from goatools.anno.gaf_reader import GafReader
from goatools.go_enrichment import GOEnrichmentStudy


chromosome = 'chr2L'

gene_map = pd.read_csv('/home/vishalr/Downloads/dictionary_fly/source/s2_gene_info.csv')

def to_dee2_id(genes = []):
    dee2_ids = []
    for gene_ix, gene in enumerate(genes):
        if(len(gene_map.index[gene == gene_map['GeneSymbol']])>0):
            dee2_ids.append(gene_map['Unnamed: 0'][gene_map.index[gene == gene_map['GeneSymbol']][0]])
    return dee2_ids

obo_loc = '/data/shared/vishal/chromatin_DL/compare_stats/code/go-basic.obo'
go_dag = obo_parser.GODag(obo_loc)

go_annotation_file = '/data/shared/vishal/chromatin_DL/compare_stats/code/fb.gaf'
go_anno = GafReader(go_annotation_file)
ns2assc = go_anno.get_ns2assc()

ensmb = pd.read_csv("/home/vishalr/Downloads/dictionary_fly/source/dm3.UCSC_genes.E1000B.promoters.bed", sep='\t', header=None)

all_genes_chr = ensmb[ensmb[0] == chromosome]

all_genes_mapped = to_dee2_id(list(set(all_genes_chr[3])))

#goeaobj = GOEnrichmentStudy(
#    ns2assc['BP'].keys(),  # List of gene symbols or IDs
#    ns2assc['BP'],  # Gene to GO annotations dictionary
#    go_dag,  # Gene Ontology DAG
#    propagate_counts=True,
#    alpha=0.05
#)

goeaobj = GOEnrichmentStudy(
    all_genes_mapped,  # List of gene symbols or IDs
    ns2assc['BP'],  # Gene to GO annotations dictionary
    go_dag,  # Gene Ontology DAG
    propagate_counts=True,
    alpha=0.05,
    methods=["bonferroni"]
)




go_count_unfiltered = []
for dict_number in range(0,25,1):
    
    
    #dict_dir = '/data/shared/vishal/chromatin_DL/compare_stats/convexMF_results/dictionaries_10/'+chromosome
    #dict_loc = dict_dir+'/representatives_dict_'+str(dict_number+1)+'_genelist.txt'
    
    
    dict_dir = '/data/shared/vishal/chromatin_DL/compare_stats/online_cvxNDL_dictionaries/'+chromosome+'/representatvies_edge_list_updated_0905_MCMC_pivot_train_iter_10k/dictionary_'+str(dict_number)
    
    #dict_dir = '/home/vishalr/Downloads/dictionary_fly/gene_lists/'+chromosome+'/dictionary_'+str(dict_number)
    dict_loc = dict_dir+'/representatives_'+chromosome+'_genelist_test.txt'

    
    
    with open(dict_loc) as f:
        lines = f.read().splitlines()
        
        
    
    
    
    gene_list = to_dee2_id(lines)
    
    
    goea_results_all = goeaobj.run_study(gene_list)
    
    # Print the results
    itr = 0
    for rec in goea_results_all:
        if(rec.get_pvalue()>0.05):
            break
        print(rec.name, rec.get_pvalue())
        #if(rec.p_uncorrected>0.05):
        #    break
        itr=itr+1
        #print(rec.name, rec.get_pvalue())
    print(itr)
    go_count_unfiltered.append(itr)
    