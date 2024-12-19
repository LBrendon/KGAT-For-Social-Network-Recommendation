# KGAT-For-Social-Network-Recommendation
This is pytorch implementation for the paper:

>Xiang Wang, Xiangnan He, Yixin Cao, Meng Liu and Tat-Seng Chua (2019). KGAT: Knowledge Graph Attention Network for Recommendation. [Paper in ACM DL](https://dl.acm.org/authorize.cfm?key=N688414) or [Paper in arXiv](https://arxiv.org/abs/1905.07854). In KDD'19, Anchorage, Alaska, USA, August 4-8, 2019.

* pytorch vision implementation by :Luna-Fu
* Tensorflow implementation by the paper authors [here](https://github.com/xiangwang1223/knowledge_graph_attention_network).
* This code was modified for transfer SNAP fackbook dataset into knowledge graph for model train.

#Environment Requirement:
Python 3.7.10
* torch == 1.6.0
* numpy == 1.21.4
* pandas == 1.3.5
* scipy == 1.5.2
* tqdm == 4.62.3
* scikit-learn == 1.0.1

### Run the Codes
* For generate the knowledge graph and train data and test run kg_generate_main under kg_generate package.
* For train the KGAT model run main_kgat.
* For train the NFM model run main_nfm.
* For train the CKE model run main_cke.
* Before you run please change the data path in kgat_parser package or use --data_dir to change the path.
