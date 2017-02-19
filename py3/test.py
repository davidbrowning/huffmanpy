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

hnodes = [hn.HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
for kv in [('A', 4), ('B', 3), ('C', 1), ('D', 1)]]
htr = h.HuffmanTree.fromListOfHuffmanTreeNodes(hnodes)

htr.encodeSymbol('C')
htr.encodeSymbol('B')
htr.encodeSymbol('D')

ut.unit_test_01()
ut.unit_test_02()
ut.unit_test_03()
ut.unit_test_04()
ut.unit_test_05()
ut.unit_test_06()
ut.unit_test_07()
ut.unit_test_08()



