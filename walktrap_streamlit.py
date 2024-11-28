import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import os
import subprocess

# Function to open a PDF file
def open_pdf(file_name):
    """
    Open the specified PDF file.
    """
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(file_name)
        elif os.name == 'posix':  # For macOS/Linux
            subprocess.run(['open', file_name], check=True)
        else:
            subprocess.run(['xdg-open', file_name], check=True)
    except Exception as e:
        st.error(f"Could not open file: {e}")

# Function to execute the Walktrap algorithm
def execute_walktrap(n, edges):
    """
    Execute the Walktrap algorithm with graph visualization.
    """
    try:
        # Create a graph and add edges
        graph = nx.Graph()
        for edge in edges:
            u, v = map(int, edge.split())
            graph.add_edge(u, v)

        # Plot the original graph
        st.subheader("Original Graph")
        fig, ax = plt.subplots()
        nx.draw(graph, with_labels=True, node_color='lightblue', node_size=500, ax=ax)
        st.pyplot(fig)

        # Community detection using a greedy modularity approach
        communities = list(nx.community.greedy_modularity_communities(graph))
        st.subheader("Detected Communities")
        for i, community in enumerate(communities, 1):
            st.write(f"Community {i}: {sorted(community)}")

        # Visualize each community
        colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']
        for i, community in enumerate(communities):
            st.subheader(f"Community {i}")
            fig, ax = plt.subplots()
            subgraph = graph.subgraph(community)
            nx.draw(subgraph, with_labels=True, node_color=colors[i % len(colors)], node_size=500, ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Main Streamlit App
st.title("Walktrap Algorithm GUI")

# PDF Section
st.subheader("Documentation")
if st.button("Open Introduction PDF"):
    open_pdf("Introduction.pdf")

if st.button("Open Details and Terminologies PDF"):
    open_pdf("Details.pdf")

# Walktrap Algorithm Section
st.subheader("Execute Walktrap Algorithm")
n = st.number_input("Enter number of nodes:", min_value=1, step=1, value=1)

edges_input = st.text_area("Enter edges (u v format, one per line):", height=200)
edges = edges_input.strip().split('\n')

if st.button("Run Walktrap Algorithm"):
    if edges_input:
        execute_walktrap(n, edges)
    else:
        st.error("Please enter at least one edge.")

# Exit Section
st.subheader("Exit")
st.button("Close Application")
