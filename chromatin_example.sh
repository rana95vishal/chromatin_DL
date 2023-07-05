#! /bin/sh
#
# chromatin_example.sh


NUMITER=1000
K_CLUSTER=25
DTYPE="iid_ndl"
VERSION=Rr
MIN_SIZE=10
EXPR_NAME=chr3R_drosophila_ChIA_Drop_0.1_PASS_20000_MCMC_pivot
RESULT_DIR="results/DNA/"
DATA_DIR="processed_data/DNA/"
PCA=-1

python -W ignore ./code/online_cvxNDL_alg.py --numIter ${NUMITER} --NF 1\
    --k_cluster ${K_CLUSTER} \
    --dtype ${DTYPE} \
	--size_min ${MIN_SIZE} \
    --expr_name ${EXPR_NAME} \
    --version ${VERSION} \
	--pca ${PCA} \
	--result_dir ${RESULT_DIR} \
	--data_dir ${DATA_DIR}
