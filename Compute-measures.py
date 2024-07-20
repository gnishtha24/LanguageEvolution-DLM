# Using NetworkX package and conllu package
import os
from io import open
from conllu import parse
import networkx as nx
from operator import itemgetter
from Measures import  Compute_measures
import random

class Compute_measures:
    def __init__(self, tree):
        self.tree = tree

    def projection_degree(self, root):
        max_depth = 0
        for node in nx.descendants(self.tree, root):
            depth = nx.shortest_path_length(self.tree, source=root, target=node)
            if depth > max_depth:
                max_depth = depth
        return max_depth

    def dependency_direction(self, edge):
        head, dependent = edge
        return 'left' if head > dependent else 'right'

    def dependency_distance(self, edge):
        head, dependent = edge
        return abs(head - dependent)

    def dependency_depth(self, edge):
        node = edge[1]
        depth = 0
        while node != 0:
            node = self.tree.nodes[node]['head']
            depth += 1
        return depth

    def num_cross_real(self):
        ncross_real = 0
        edges = list(self.tree.edges)
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                if self.do_edges_cross(edges[i], edges[j]):
                    ncross_real += 1
        return ncross_real

    def do_edges_cross(self, edge1, edge2):
        (a, b) = edge1
        (c, d) = edge2
        return (a < c < b < d) or (c < a < d < b)




directory = "./SUD"  # directory containing the UD scheme tree files in CONLLU format
ud_files = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.conllu'):
            fullpath = os.path.join(root, file)
            ud_files.append(fullpath)  # creates a list of path of all files (file of each language) from the directory

for i in ud_files:  # reads file of each language one by one
    lang = str(i)
    dfile = open(lang, 'r', encoding='utf-8')
    data_file = dfile.read()
    sentences = []
    sent_id = 0
    print(lang)
    num_sent = 0
    num_edge = 0
    sentences = data_file.split('\n\n')
    print(sentences)
    for sentence in sentences:
        sent_id += 1
        lines = sentence.strip().split('\n')
        tree = nx.DiGraph()
        for line in lines:
            if line.startswith('#'):
                continue
            parts = line.split('\t')
            print(parts)
            node_id = parts[0]
            if len(parts) > 5:
                if not parts[6] == 'punct':
                    tree.add_node(int(node_id), form=parts[1], lemma=parts[2], upostag=parts[3], xpostag=parts[4], head=int(parts[5]), deprel=parts[6])  # adds node to the directed graph
        ROOT = 0
        tree.add_node(ROOT)  # adds an abstract root node to the directed graph

        for nodex in tree.nodes:
            if not nodex == 0:
                if tree.has_node(tree.nodes[nodex]['head']):  # to handle disjoint trees
                    tree.add_edge(tree.nodes[nodex]['head'], nodex, drel=tree.nodes[nodex]['deprel'])  # adds edges as relation between nodes
        print(tree.edges)
        n = len(tree.edges)
        if n < 30 and n > 1:
            get = Compute_measures(tree)
            # Computes the measures for the real tree
            projection_degree_real = get.projection_degree(0)  # gives the projection degree of the tree i.e., size of longest projection chain in the tree
            sent_len = 0
            for edgey in tree.edges:
                if not edgey[0] == 0:
                    direction_real = get.dependency_direction(edgey)  # direction of the edge in terms of relative linear order of head and its dependent
                    dep_distance_real = get.dependency_distance(edgey)  # gives the distance between nodes connected by an edge
                    dep_depth_real = get.dependency_depth(edgey)
                    results2 = open('English-measures.csv', 'a')
                    results2.write(str(lang) + "\t" + "real" + "\t" + str(sent_id) + "\t" + str(n) + "\t" + str(projection_degree_real) + "\t" + str(edgey) + "\t" + str(direction_real) + "\t" + str(dep_distance_real) + "\t" + str(dep_depth_real) + "\n")
                    results2.close()
                print("\n-----------------\n" + str(tree.edges))

            # Calculate number of crossings in the real tree
            num_crossings_real = get.num_cross_real()
            print("Number of crossings in the real tree:", num_crossings_real)

            # Generate random trees
            random_base = Random_base(tree)
            random_trees = random_base.gen_random(num_crossings_real)
            print("Generated random trees:", random_trees)
