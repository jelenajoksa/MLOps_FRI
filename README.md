# Sample model 

![Unit tests](https://github.com/FRI-Machine-Learning-Operations-22-23/mlops-01-hands-on/actions/workflows/test-package.yml/badge.svg)

Test repo for hands-on part of the first MLOps lecture.


## How to use it



```python
from mlops_models import ConstantPredictionModel

model = ConstantPredictionModel(0)
model.predict("")
> 0
```


```python
from mlops_models import ConstantPredictionModel

model = ConstantPredictionModel(1)
model.predict("")
> 1
```


## How to develop

TBD
