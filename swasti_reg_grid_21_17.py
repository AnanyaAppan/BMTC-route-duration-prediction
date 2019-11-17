import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from smac.configspace import ConfigurationSpace 
from ConfigSpace.hyperparameters import UniformIntegerHyperparameter
from smac.tae.execute_func import ExecuteTAFuncDict
from smac.scenario.scenario import Scenario
from smac.facade.smac_hpo_facade import SMAC4HPO

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('encoded_grid_21_17.csv', header=None, nrows = 10000)

train=df.sample(frac=0.8,random_state=42) #random state is a seed value
test=df.drop(train.index)

X = train.iloc[:,[2,3,4,7]].values
y = train.iloc[:,5].values
# print(X.shape)
# print(y.shape)

cs = ConfigurationSpace()
deg = UniformIntegerHyperparameter("deg", 2, 5, default_value = 3)
comp = UniformIntegerHyperparameter("comp", 1, 20, default_value = 10)
cs.add_hyperparameters([deg, comp])

def model_from_cfg(cfg):

    poly = PolynomialFeatures(degree = cfg['deg']) 
    X_poly = poly.fit_transform(X)
    X_poly = StandardScaler().fit_transform(X_poly)
    # print(X_poly.shape[1])

    cfg["comp"] = min(cfg["comp"], X_poly.shape[1])

    cols = ['principal component ' + str(x) for x in range(1,cfg["comp"]+1)]
    pca = PCA(n_components=cfg["comp"])
    principalComponents = pca.fit_transform(X_poly)
    X_poly = pd.DataFrame(data = principalComponents , columns = cols)
    
    poly.fit(X_poly, y) 
    lin2 = LinearRegression() 

    scores = cross_val_score(lin2, X_poly, y, cv=5)
    return np.mean(scores)
    
scenario = Scenario({
    "run_obj" : "quality",
    "wallclock_limit" : 5,
    "cs" : cs,
    "deterministic" : "true"
})

def_value = model_from_cfg(cs.get_default_configuration())
print("Default value : ", def_value)

smac = SMAC4HPO(scenario=scenario, rng=np.random.RandomState(42), tae_runner=model_from_cfg)

incumbent = smac.optimize()

inc_value = model_from_cfg(incumbent)

print("Optimized Value : ", inc_value)


