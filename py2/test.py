#!/usr/bin/python

import BinHuffmanTree as b
import BinHuffmanTreeNode as bn
import CharFreqMap as c
import HuffmanTree as h
import HuffmanTreeNode as hn
import unit_tests as ut

hn1 = hn.HuffmanTreeNode(symbols=set(['A']), weight=8)
print(str(hn1))
print(hn1.getSymbols())
print(hn1.getWeight())
print(hn1.isLeaf())
hn2 = hn.HuffmanTreeNode(symbols=set(['B']), weight=3)
print(hn1 == hn2)
hn3 = hn.HuffmanTreeNode(symbols=set(['A']), weight=8)
print(hn1 == hn3)


