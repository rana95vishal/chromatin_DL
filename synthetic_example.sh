#! /bin/sh
#
# synthetic_example.sh
# Copyright (C) 2019 jianhao2 <jianhao2@illinois.edu>
#
# Distributed under terms of the MIT license.
#

NUMITER=1000
K_CLUSTER=3
LMDA=0
DTYPE="sbm"
CANDIDATE=5
MIN_SIZE=3
VERSION=Rr
PCA=-1
EXPR_NAME=sbm2_1000_MCMC_pivot
RESULT_DIR="results/synthetic/"
DATA_DIR="processed_data/synthetic/"

python -W ignore ./code/online_cvxNDL_alg.py --numIter ${NUMITER} --NF 1 \
    --lmda ${LMDA} \
    --k_cluster ${K_CLUSTER} \
    --dtype ${DTYPE} \
    --candidate_size ${CANDIDATE} \
    --expr_name ${EXPR_NAME} \
    --size_min ${MIN_SIZE} \
    --version ${VERSION} \
    --pca ${PCA} \
	--result_dir ${RESULT_DIR} \
	--data_dir ${DATA_DIR}
