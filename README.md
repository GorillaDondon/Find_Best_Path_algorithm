# Genetic Algorithms - Graph Miner

This project implements a graph mining tool using a genetic algorithm approach in Python. Given a network graph and a subset of nodes, the tool seeks to find a minimum-cost subgraph that connects the designated nodes. A visualization of the final solution is provided through a front-end to aid in understanding the results and cost analysis.

## Overview

This project uses genetic algorithms to solve a graph mining problem. By taking a network graph and a subset of nodes, the tool evolves potential solutions to find the minimum-cost subgraph that connects all given nodes. The visualization of the final solution highlights the selected nodes and links, and displays relevant cost information for easy interpretation.

## Problem Description
- Graph (G = (N, L)):
  - N: Set of nodes.
  - L: Set of links between nodes.
- Subgraph (G' = (N', L')):
  - The goal is to find a subgraph that:
    - Includes a subset of nodes 𝑀 ⊆ 𝑁
    - Minimizes the number of links |L'|
- Cost Calculation:
  - The cost of a solution subgraph is measured by the number of links |L'| included.
 
## Features
- Genetic Algorithm-Based Optimization: The program uses genetic algorithms to find a minimum-cost subgraph.
- Progress Tracking: Displays progress after each generation, including:
  - Number of generations completed
  - Current best solutions and their costs
- Front-End Visualization: Visualizes the network graph with labeled nodes and links, highlighting the subgraph solution.
- Flexible Input: Takes input from a network graph description file, making it adaptable for different graphs.


### Useful links 

[Slide (mutation)](https://liacs.leidenuniv.nl/~nijssensgr/CI/2013/10%20genetic%20algorithm.pdf) 

[Slide (encoding)](https://cse.iitkgp.ac.in/~dsamanta/courses/sca/resources/slides/11%20EC%20Encoding.pdf) 
