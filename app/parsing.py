import os
import json
import csv

def parse_files(metadata_file, technical_file):
    # Parse technical file (plain text)
    with open(technical_file, 'r', encoding='utf-8') as file:
        passages = file.readlines()

    # Parse metadata file (JSON)
    with open(metadata_file, 'r', encoding='utf-8') as file:
        metadata_data = json.load(file)
        metadata = metadata_data  # Access metadata directly, without 'metadata' key

    # Combine passages and metadata
    combined_data = list(zip(passages, [json.dumps(metadata)] * len(passages)))

    # Write to CSV
    with open('passage_metadata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Passage', 'Metadata'])
        csvwriter.writerows(combined_data)
# File paths
file_paths = [
    {"metadata_file":"Corpus/kwame-legal-EL-1680770407105_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770407105_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770408447_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770408447_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770435319_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770435319_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770436197_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770436197_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770441330_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770441330_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770603145_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770603145_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770614137_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770614137_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770618503_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770618503_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770618884_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770618884_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770620345_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770620345_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770674774_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770674774_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770764365_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770764365_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-EL-1680770776743_Metadata.json", "technical_file":"Corpus/kwame-legal-EL-1680770776743_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-G-1680770761086_Metadata.json",  "technical_file":"Corpus/kwame-legal-G-1680770761086_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-G-1680770817291_Metadata.json",  "technical_file":"Corpus/kwame-legal-G-1680770817291_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-G-1680770887862_Metadata.json",  "technical_file":"Corpus/kwame-legal-G-1680770887862_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770244872_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770244872_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770264876_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770264876_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770283606_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770283606_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770283815_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770283815_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770288959_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770288959_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770292495_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770292495_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770305200_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770305200_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770310611_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770310611_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770336730_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770336730_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770336937_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770336937_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770339583_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770339583_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770339801_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770339801_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-GLR-1680770411932_Metadata.json", "technical_file":"Corpus/kwame-legal-GLR-1680770411932_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770534633_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770534633_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770566127_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770566127_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770637908_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770637908_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770655350_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770655350_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770692801_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770692801_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770715462_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770715462_Technical.txt"},
    {"metadata_file":"Corpus/kwame-legal-LG-1680770745754_Metadata.json",  "technical_file":"Corpus/kwame-legal-LG-1680770745754_Technical.txt"},
]

for data in file_paths:
    parse_files(data["metadata_file"], data["technical_file"])