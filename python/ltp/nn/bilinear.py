#! /usr/bin/env python
# -*- coding: utf-8 -*_
# Author: Yunlong Feng <ylfeng@ir.hit.edu.cn>
import torch, math
from torch import nn, Tensor
from torch.nn import functional as F


# Change from Pytorch nn.Bilinear
class Bilinear(nn.Module):
    __constants__ = ['in1_features', 'in2_features', 'out_features', 'bias_x', 'bias_y']

    def __init__(self, in1_features, in2_features, out_features, expand=False, bias_x=True, bias_y=True):
        super(Bilinear, self).__init__()
        self.expand = expand
        self.bias_x = bias_x
        self.bias_y = bias_y
        self.in1_features = in1_features
        self.in2_features = in2_features
        self.out_features = out_features
        self.weight = nn.Parameter(
            torch.zeros(out_features, in1_features + bias_x, in2_features + bias_y),
            requires_grad=True
        )
        self.reset_parameters()

    def reset_parameters(self):
        bound = 1 / math.sqrt(self.weight.size(1))
        nn.init.uniform_(self.weight, -bound, bound)

    def onnx_forward(self, x1: Tensor, x2: Tensor):
        if self.bias_x:
            x1 = torch.cat((x1, torch.ones_like(x1[..., :1])), -1)
        if self.bias_y:
            x2 = torch.cat((x2, torch.ones_like(x2[..., :1])), -1)
        x1 = x1.unsqueeze(1)
        x2 = x2.unsqueeze(1)
        s: Tensor = x1 @ self.weight @ x2.transpose(-1, -2)
        if s.size(1) == 1:
            s = s.squeeze(1)
        return s

    def forward(self, x1: Tensor, x2: Tensor):
        res = self.onnx_forward(x1, x2)
        if self.bias_x:
            x1 = torch.cat((x1, torch.ones_like(x1[..., :1])), -1)
        if self.bias_y:
            x2 = torch.cat((x2, torch.ones_like(x2[..., :1])), -1)
        if self.expand:
            # [batch_size, n_out, seq_len, seq_len]
            s = torch.einsum('bxi,oij,byj->boxy', x1, self.weight, x2)
            test = torch.sum(s - res)
            return s
        # [batch_size, n_out, seq_len]
        return F.bilinear(x1, x2, self.weight, None)

    def extra_repr(self):
        return 'in1_features={}, in2_features={}, out_features={}, bias_x={}, bias_y={}'.format(
            self.in1_features, self.in2_features, self.out_features, self.bias_x, self.bias_y
        )
