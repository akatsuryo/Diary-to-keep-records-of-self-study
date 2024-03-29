# -*- coding: utf-8 -*-
"""networkを用いた機械学習.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YwhAHPTz2X6ILJsBa6xXSjV5xqHbFB8e
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

#sklearnのデータセット。アイリス（花）の種類を分類
#回帰などの場合はload_diabetes()という糖尿病の進行状況のデータなどを使用する。
#参考https://note.nkmk.me/python-sklearn-datasets-load-fetch/

from sklearn.datasets import load_iris

iris=load_iris()

#入力値と目標値を抽出
x=iris['data']
t=iris['target']

iris

type(x),type(t)

#numpy型からtensor型に変換
x=torch.tensor(x,dtype=torch.float32)
t=torch.tensor(t,dtype=torch.int64)

#<ipython-input-10-34d329a9c3fc>:2: UserWarning:
# テンソルから構造をコピーするには、sourceTensor.clone().detach() または
#sourceTensor.clone().detach().requires_grad_(True) を使用することをお勧めします。

type(x),type(t)

#(torch.Size([150, 4]), torch.Size([150]))と出力される。見方としては、
#torch.Size([150, 4]＝アイリスの種類が150種類で入力値が4種類あるということ。
#torch.Size([150]=
x.shape, t.shape

