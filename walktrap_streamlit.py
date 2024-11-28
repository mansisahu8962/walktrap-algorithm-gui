import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import os
import subprocess

# Function to open a PDF file from Google Drive
def open_pdf_from_google_drive(file_id):
    """
    Generate a direct download link from Google Drive for the provided file ID.
    """
    pdf_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    st.markdown(f"Click [here]( {pdf_url} ) to download the PDF.")

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
# Use the Google Drive file IDs in place of file names
if st.button("Open Introduction PDF"):
    # Replace 'FILE_ID' with your actual Google Drive file ID
    open_pdf_from_google_drive("1CAkOzXQ64m3M1IPGJ3vG3qKPDMbnIxYV")

if st.button("Open Details and Terminologies PDF"):
    # Replace 'FILE_ID' with your actual Google Drive file ID for Details PDF
    open_pdf_from_google_drive("10iNfcGGkEqqJsX-ArnZ-g-OA0jy0ENTJ")  # Change this if the file ID is different for the second PDF

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