#!/usr/bin/python

######################################
## module: HuffmanTreeNode.py
## David Browning
## A01256705
######################################

from HuffmanTreeNode import HuffmanTreeNode

class HuffmanTree(object):
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def traverse(self, node, e_char):
        if(node is None):
            return
        print(node.getSymbols())
        HuffmanTree.traverse(self, node.getLeftChild(), e_char)
        HuffmanTree.traverse(self, node.getRightChild(), e_char)

    def determineEncoding(self, node, e_char, s_char):
        if(node is None):
            return
        b = True
        for s in node.getSymbols():
            if s == s_char:
                b = False
        if(b == True):
            e_char.pop()
            return
        if(node.isLeaf()):
            return
        e_char.append('0')
        HuffmanTree.determineEncoding(self, node.getLeftChild(), e_char, s_char)
        e_char.append('1')
        HuffmanTree.determineEncoding(self, node.getRightChild(), e_char, s_char)

    def encodeSymbol(self, s):
        if not s in self.__root.getSymbols():
            raise Exception('Unknown symbol')
        else:
            encoded_character =[]
            curr_node = self.getRoot()
            HuffmanTree.determineEncoding(self, curr_node, encoded_character, s)
            return(''.join(encoded_character))

    def encodeText(self, txt):
        enc_txt = ''
        for a in txt:
            enc_txt += HuffmanTree.encodeSymbol(self, a)

        return enc_txt

    def decode(self, bin_string):
        end_string = ''
        node = self.getRoot()
        for c in bin_string:
            #print(node.getSymbols())
            if(c == '0'):
                node = node.getLeftChild()
                if(node.isLeaf()):
                    end_string += next(iter(node.getSymbols()))
                    node = self.getRoot()
            elif(c == '1'):
                node = node.getRightChild()
                if(node.isLeaf()):
                    end_string += next(iter(node.getSymbols()))
                    node = self.getRoot()
        return end_string


    @staticmethod
    def mergeTwoNodes(htn1, htn2):
        #print 'Merging', str(htn1), str(htn2)
        symbols = set(htn1.getSymbols())
        for i in htn2.getSymbols():
            symbols.add(i)
        n = HuffmanTreeNode(symbols=symbols, weight=htn1.getWeight() + htn2.getWeight())
        if(htn1.isLeaf() and htn2.isLeaf()):
            if(next(iter(htn1.getSymbols())) > next(iter(htn2.getSymbols()))):
                tmp = htn1;
                htn1 = htn2;
                htn2 = tmp;
        n.setLeftChild(htn1)
        n.setRightChild(htn2)
        return n

    @staticmethod
    def findTwoLowestWeightNodes(list_of_nodes):
        return(list_of_nodes.pop(), list_of_nodes.pop())
        pass

    @staticmethod
    def displayListOfNodes(list_of_nodes):
        for n in list_of_nodes:
            print(str(n))

    @staticmethod
    def fromListOfHuffmanTreeNodes(list_of_nodes):
        if len(list_of_nodes) == 0:
            raise Exception('Cannot construct from empty list of nodes')
        elif len(list_of_nodes) == 1:
            return HuffmanTree(root=list_of_nodes[0])
        else:
            while(len(list_of_nodes) > 1):
                list_of_nodes = sorted(list_of_nodes, key=lambda n:n.getWeight(), reverse=True)
                n = HuffmanTree.findTwoLowestWeightNodes(list_of_nodes)
                nn = HuffmanTree.mergeTwoNodes(n[0], n[1])
                list_of_nodes.append(nn)
            return HuffmanTree(root = list_of_nodes.pop())


    @staticmethod
    def freqMapToListOfHuffmanTreeNodes(freq_map):
        return [HuffmanTreeNode(symbols=set([item[0]]), weight=item[1]) for item in freq_map.items()]



