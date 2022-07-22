import os
import pytest
import pandas as pd
import shutil
from os.path import dirname, abspath
from GenNet_utils.Create_plots import  sunburst_plot, plot_layer_weight, manhattan_relative_importance
from GenNet_utils.Utility_functions import get_paths

# import unittest
# TODO: add test without covariates
# TODO add test with covariates for regression + classification
# TODO add test with multiple genotype files.
# test randomnesss after .. epoch shuffles.


def get_GenNet_path():
    return str(dirname(dirname(abspath(__file__)))) + "/"

def remove_old_test(ID):
    GenNet_path  =  get_GenNet_path()
    resultpath = GenNet_path +  "results/GenNet_experiment_" + str(ID)  + '_/'
    try:
        shutil.rmtree(resultpath)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        return str(dirname(dirname(abspath(__file__)))) + "/"


class ArgparseSimulator():
    def __init__(self,
                 path='/',
                 ID=999,
                 genotype_path='undefined',
                 network_name='undefined',
                 problem_type="classification",
                 wpc=1,
                 lr=0.01,
                 bs=10,
                 epochs=10,
                 L1=0.001,
                 patience = 10,
                 epoch_size = 100,
                 mixed_precision=False,
                 outfolder="undefined",
                 suffix=''):
        self.path = path
        self.ID = ID
        self.genotype_path = genotype_path
        self.network_name = network_name
        self.problem_type = problem_type
        self.wpc = wpc
        self.lr = lr
        self.learning_rate = lr
        self.bs = bs
        self.batch_size = bs
        self.epochs = epochs
        self.L1 = L1
        self.mixed_precision = mixed_precision
        self.out = outfolder
        self.suffix = suffix
        self.patience = patience
        self.epoch_size = epoch_size
        


class TestAtoZ():       
    def test_convert(self):
        GenNet_path = get_GenNet_path()
        test1 = os.system(
            "python {}/GenNet.py convert -g {}/examples/A_to_Z/plink/"
            " -o {}/examples/A_to_Z/processed_data/"
            "/  -study_name GenNet_simulation -step all".format(GenNet_path, GenNet_path, GenNet_path) )
        assert test1 == 0
        
#         !python GenNet.py topology -type create_annovar_input -path ./examples/A_to_Z/processed_data/ -study_name GenNet_simulation -out examples/A_to_Z/processed_data/

# !python GenNet.py topology -type create_gene_network -path examples/A_to_Z/processed_data/ -out examples/A_to_Z/processed_data/ -study_name GenNet_simulation


# mkdir examples/A_to_Z/new_run_folder/
# mv examples/A_to_Z/processed_data/SNP_gene_mask.npz  examples/A_to_Z/new_run_folder/ # or topology.csv
# mv examples/A_to_Z/processed_data/genotype.h5  examples/A_to_Z/new_run_folder/
# cp examples/A_to_Z/run_folder/subjects.csv  examples/A_to_Z/new_run_folder/ 


# !python GenNet.py train -path examples/A_to_Z/new_run_folder/ -ID 100001 -epochs 50

# !python GenNet.py plot -ID 100001 -type manhattan_relative_importance 

class TestTrain():
    def test_train_classification(self): 
        remove_old_test(999999999)
        GenNet_path = get_GenNet_path()
        value = os.system('python {}/GenNet.py train -path {}/examples/example_classification/ -ID 999999999 -epochs 2'.format(GenNet_path, GenNet_path) )
        assert value == 0

    def test_train_regression(self):
        remove_old_test(999999998)
        GenNet_path = get_GenNet_path()
        value = os.system('python {}/GenNet.py train -path {}/examples/example_regression/ -ID 999999998 -problem_type regression -epochs 2'.format(GenNet_path, GenNet_path) )
        assert value == 0        
        

@pytest.mark.parametrize("ID", [999999999, 999999998]) # test both regression and classification
class TestPlot():       
    def test_sunburst(self, ID):
        GenNet_path  =  get_GenNet_path()
        resultpath = GenNet_path +  "results/GenNet_experiment_" + str(ID)  + '_/'
        importance_csv = pd.read_csv(resultpath + "/connection_weights.csv", index_col=0)
        sunburst_plot(resultpath, importance_csv)
        
    def test_manhattan(self, ID):
        GenNet_path  =  get_GenNet_path()
        resultpath = GenNet_path +  "results/GenNet_experiment_" + str(ID)  + '_/'
        importance_csv = pd.read_csv(resultpath + "/connection_weights.csv", index_col=0)
        manhattan_relative_importance(resultpath, importance_csv)
        
    def test_plot_layer_weight_1(self, ID):
        GenNet_path  =  get_GenNet_path()
        resultpath = GenNet_path +  "results/GenNet_experiment_" + str(ID)  + '_/'
        importance_csv = pd.read_csv(resultpath + "/connection_weights.csv", index_col=0)
        plot_layer_weight(resultpath, importance_csv, layer=0)
    def test_plot_layer_weight_2(self, ID):
        GenNet_path  =  get_GenNet_path()
        resultpath = GenNet_path +  "results/GenNet_experiment_" + str(ID)  + '_/'
        importance_csv = pd.read_csv(resultpath + "/connection_weights.csv", index_col=0)
        plot_layer_weight(resultpath, importance_csv, layer=1)
    

# @pytest.mark.parametrize("ID", [999999999, 999999998]) # test both regression and classification      
# class CheckAllFiles():
#     def trainin_files(self, ID):
    

