# File: autojob/src/keywords/ex_textacy.py

import os
import sys
import spacy
import textacy

# Constants for sCAKE Algorithm
TOP_N_SCAKE = 10  # Specifies the number of top-ranked terms to return (default: 10)
NORMALIZE_SCAKE = "lemma"  # Specifies the normalization method for sCAKE
INCLUDE_POS_SCAKE = ['NOUN', 'PROPN', 'ADJ']  # Specifies POS tags for sCAKE

# Constants for TextRank method
WINDOW_SIZE_TEXTRANK = 2
EDGE_WEIGHTING_TEXTRANK = "binary"
POSITION_BIAS_TEXTRANK = False
TOP_N_TEXTRANK = 10
NORMALIZE_TEXTRANK = "lemma"  # Specifies the normalization method for TextRank
INCLUDE_POS_TEXTRANK = ['NOUN', 'PROPN', 'ADJ']  # Specifies POS tags for TextRank

# Constants for SingleRank method
WINDOW_SIZE_SINGLERANK = 10
EDGE_WEIGHTING_SINGLERANK = "count"
POSITION_BIAS_SINGLERANK = False
TOP_N_SINGLERANK = 10
NORMALIZE_SINGLERANK = "lemma"  # Specifies the normalization method for SingleRank
INCLUDE_POS_SINGLERANK = ['NOUN', 'PROPN', 'ADJ']  # Specifies POS tags for SingleRank

# Constants for PositionRank method
WINDOW_SIZE_POSITIONRANK = 10
EDGE_WEIGHTING_POSITIONRANK = "count"
POSITION_BIAS_POSITIONRANK = True
TOP_N_POSITIONRANK = 10
NORMALIZE_POSITIONRANK = "lemma"  # Specifies the normalization method for PositionRank
INCLUDE_POS_POSITIONRANK = ['NOUN', 'PROPN', 'ADJ']  # Specifies POS tags for PositionRank

def ke_txcy_scake(doc, topn=TOP_N_SCAKE, normalize=NORMALIZE_SCAKE, include_pos=INCLUDE_POS_SCAKE):
    """
    Extracts key terms from a document using the sCAKE algorithm.

    Parameters:
    - doc: The input document.
    - topn: Number of top-ranked terms to return (default: 10).
    - normalize: Specifies the normalization method for key terms. Options: "lemma" (default), "lower", None, or a custom callable.
    - include_pos: One or more POS tags with which to filter for good candidate keyterms. Default is ('NOUN', 'PROPN', 'ADJ').

    Returns:
    List of top-ranked key terms.
    """
    keyterms_scake = textacy.extract.keyterms.scake(
        doc,
        topn=topn,
        normalize=normalize,
        include_pos=include_pos
    )
    return keyterms_scake

def ke_txcy_textrank(doc, normalize=NORMALIZE_TEXTRANK, include_pos=INCLUDE_POS_TEXTRANK):
    """
    Extracts key terms from a document using the TextRank algorithm.

    Parameters:
    - doc: The input document.
    - normalize: Specifies the normalization method for key terms. Options: "lemma" (default), "lower", None, or a custom callable.
    - include_pos: One or more POS tags with which to filter for good candidate keyterms. Default is ('NOUN', 'PROPN', 'ADJ').
    - window_size: Size of sliding window in which term co-occurrences are determined. Default is 2.
    - edge_weighting: If "count", the nodes for all co-occurring terms are connected by edges with weight equal to the number of times they co-occurred within a sliding window; if "binary", all such edges have weight = 1. Default is "binary".
    - position_bias: If True, bias the PageRank algorithm for weighting nodes in the word graph, such that words appearing earlier and more frequently in doc tend to get larger weights. Default is False.
    - topn: Number of top-ranked terms to return as key terms. If an integer, represents the absolute number; if a float, value must be in the interval (0.0, 1.0], which is converted to an int by int(round(len(set(candidates)) * topn)). Default is 10.

    Returns:
    List of top-ranked key terms.
    """
    keyterms_textrank = textacy.extract.keyterms.textrank(
        doc,
        window_size=WINDOW_SIZE_TEXTRANK,
        edge_weighting=EDGE_WEIGHTING_TEXTRANK,
        position_bias=POSITION_BIAS_TEXTRANK,
        topn=TOP_N_TEXTRANK,
        normalize=normalize,
        include_pos=include_pos
    )
    return keyterms_textrank

def ke_txcy_singlerank(doc, normalize=NORMALIZE_SINGLERANK, include_pos=INCLUDE_POS_SINGLERANK):
    """
    Extracts key terms from a document using the SingleRank algorithm.

    Parameters:
    - doc: The input document.
    - normalize: Specifies the normalization method for key terms. Options: "lemma" (default), "lower", None, or a custom callable.
    - include_pos: One or more POS tags with which to filter for good candidate keyterms. Default is ('NOUN', 'PROPN', 'ADJ').
    - window_size: Size of sliding window in which term co-occurrences are determined. Default is 10.
    - edge_weighting: If "count", the nodes for all co-occurring terms are connected by edges with weight equal to the number of times they co-occurred within a sliding window; if "binary", all such edges have weight = 1. Default is "count".
    - position_bias: If True, bias the PageRank algorithm for weighting nodes in the word graph, such that words appearing earlier and more frequently in doc tend to get larger weights. Default is False.
    - topn: Number of top-ranked terms to return as key terms. If an integer, represents the absolute number; if a float, value must be in the interval (0.0, 1.0], which is converted to an int by int(round(len(set(candidates)) * topn)). Default is 10.

    Returns:
    List of top-ranked key terms.
    """
    keyterms_singlerank = textacy.extract.keyterms.textrank(
        doc,
        window_size=WINDOW_SIZE_SINGLERANK,
        edge_weighting=EDGE_WEIGHTING_SINGLERANK,
        position_bias=POSITION_BIAS_SINGLERANK,
        topn=TOP_N_SINGLERANK,
        normalize=normalize,
        include_pos=include_pos
    )
    return keyterms_singlerank

def ke_txcy_positionrank(doc, normalize=NORMALIZE_POSITIONRANK, include_pos=INCLUDE_POS_POSITIONRANK):
    """
    Extracts key terms from a document using the PositionRank algorithm.

    Parameters:
    - doc: The input document.
    - normalize: Specifies the normalization method for key terms. Options: "lemma" (default), "lower", None, or a custom callable.
    - include_pos: One or more POS tags with which to filter for good candidate keyterms. Default is ('NOUN', 'PROPN', 'ADJ').
    - window_size: Size of sliding window in which term co-occurrences are determined. Default is 10.
    - edge_weighting: If "count", the nodes for all co-occurring terms are connected by edges with weight equal to the number of times they co-occurred within a sliding window; if "binary", all such edges have weight = 1. Default is "count".
    - position_bias: If True, bias the PageRank algorithm for weighting nodes in the word graph, such that words appearing earlier and more frequently in doc tend to get larger weights. Default is True.
    - topn: Number of top-ranked terms to return as key terms. If an integer, represents the absolute number; if a float, value must be in the interval (0.0, 1.0], which is converted to an int by int(round(len(set(candidates)) * topn)). Default is 10.

    Returns:
    List of top-ranked key terms.
    """
    keyterms_positionrank = textacy.extract.keyterms.textrank(
        doc,
        window_size=WINDOW_SIZE_POSITIONRANK,
        edge_weighting=EDGE_WEIGHTING_POSITIONRANK,
        position_bias=POSITION_BIAS_POSITIONRANK,
        topn=TOP_N_POSITIONRANK,
        normalize=normalize,
        include_pos=include_pos
    )
    return keyterms_positionrank
