# chromatin_DL
This is a repository for the paper "Online Convex Network Dictionary Learning for Inferring Chromatin Interactions." Online cvxNDL can learn dictionary elements (i.e. cluster representatives) from extensive datasets due to its online nature. The dictionary elements are represented as convex combinations of observed data points, thus making the results interpretable and highly useful for biological applications.

<p align="center">
<img src="https://github.com/rana95vishal/chromatin_DL/blob/main/figures/dict_org_alt.png" width="600">
</p>

The algorithm has two major components: an MCMC-based network subsampling and an iterative optimization to learn the dictionary. We separated the MCMC sampling procedure for generating online samples from the iterative optimization procedure to improve the overall efficiency. The MCMC sampling procedure can be found in the folder `sampling`.

## Scripts to replicate individual steps of the pipeline

1. Clique expansion - 'code\clique_expansion.py' - If your input network is a hypergraph, convert all hyperedges to cliques. This step is necessary for data generated using ChIA-Drop where multiway chromatin interactions are captured. Pairwise contact capture protocols like Hi-C and ChIA-PET do not need to be clique-expanded.
3. MCMC sampling of subnetworks - 'sampling\generate_iid_samples.py', 'sampling\generate_synthetic_sample.py' - This step is necessary to generate online samples of subnetwork patches for the algorithm. If your dataset is presented as an online stream of subnetworks, you do not need to perform this step.
4. Online cvxNDL algorithm - 'code/online_cvxNDL_alg.py' - Implementation of the online cvxNDL algorithm as well as NDL, online NDL, and CMF for comparison.
5. Chromatin-specific GO - 'code/goa_cmf.py' - Gene Ontology analysis based on the individual chromosomes of Drosophila Melanogaster.

## Example with Synthetic Data

We provide synthetic data generated by the Stochastic Block Model (SBM) for verification. To run just the optimization step for quick verification on the synthetic dataset, use
```
source synthetic_example.sh
```
### Details of the pipeline

1. Raw data in the form of lists of edges for various SBM networks can be found in the sub-folder 'sampling\Data\synthetic\'. The sbm2 network file is plotted below
   <p align="center">
   <img src="https://github.com/rana95vishal/chromatin_DL/blob/main/figures/sbm_show.png" width="600">
   </p>
2. To run the MCMC sampling procedure, use the script 'sampling\generate_synthetic_samples.py'. The sampled data is stored in the folder 'processed_data\synthetic'.
3. To run the optimization procedure to learn the dictionary, use the 'synthetic_example.sh' script. The results will be stored in the folder 'results\synthetic'. We show one of the representative elements of the dictionary learned by our method.
   <p align="center">
   <img src="https://github.com/rana95vishal/chromatin_DL/blob/main/figures/sbm_show_reps.png" width="600">
   </p>

## ChIA-Drop Data
To download the full ChIA-Drop dataset, please refer to this [link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109355). We used the data from the RNAPII-enriched ChIA-Drop experiment (GSM3347525). 

### Pre-processing 
1. Run [MIA-Sig](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1868-z) enrichment with FDR 0.1. The required software repository can be found [here](https://github.com/TheJacksonLaboratory/mia-sig).
2. Perform clique expansion on the filtered hyperedges to obtain a regular network. After clique expansion, we have a list of edges for each chromosome and we can follow the steps in the previous example.

### Details of the pipeline
3. We provide an example with a small subset of processed data from chr3R. The list of edges is provided in the sub-folder 'sampling\Data\DNA\'.
4. Run the MCMC sampling procedure, using the script 'sampling\generate_iid_samples.py'. The sampled data is stored in the folder 'processed_data\DNA'.
5. Run the optimization procedure to learn the dictionary, using the 'chromatin_example.sh' script. The results will be stored in the folder 'results\DNA'.

## Packages
The following packages are needed to run the code
```
python=3.8
pandas
matplotlib
ipdb
tqdm
scikit-learn
k-means-constrained
cvxpy
networkx
tensorly
psutil
```
