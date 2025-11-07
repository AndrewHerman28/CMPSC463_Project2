import pickle
import os
import geopandas as gpd
from Visualization.Roadmap import roadmap_visualization, roadmap_evacuation_centers
from Algorithms.Dijkstra import dijkstra

evacuation_centers = gpd.read_file(
    "/Users/andrewherman/CMP463/Project 2/Data/Raw/philadelphia_evacuation_centers.geojson")

if os.path.exists("/Users/andrewherman/CMP463/Project 2/Data/evacuation_graph.pkl"):
    with open("/Users/andrewherman/CMP463/Project 2/Data/evacuation_graph.pkl", "rb") as f:
        G = pickle.load(f)

if G:
    roadmap_evacuation_centers(G.graph, evacuation_centers)

