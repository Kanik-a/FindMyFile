import os, re
from rapidfuzz import process, fuzz, utils
def process_text(text, base_path="C:/Users/kanik/OneDrive/Desktop"):
    print(f"Processing: {text}")
    file_index = build_file_index(base_path)
    matched_paths = searchFile(text, file_index)
    return matched_paths




def build_file_index(base_path):
    """
    Walk through base_path and build a list of file records:
    Each record is a dict with file_name (lowercased),
    parent_folder name, and full_path.
    """
    file_records = []

    for root, dirs, files in os.walk(base_path):
        parent_folder = os.path.basename(root)
        for f in files:
            file_name = f.lower()
            file_records.append({
                "file_name": file_name,
                "parent_folder": parent_folder,
                "full_path": os.path.join(root, f)
            })

    return file_records



def preprocess_file_name(filename):
    """
    Normalize file name for better fuzzy matching:
    lowercase, replace symbols with spaces, collapse spaces.
    """
    filename = filename.lower()
    #filename = re.sub(r"[_\-.,:;!?()]+", " ", filename)
    filename = re.sub(r"[^a-zA-Z0-9]+", " ", filename)
    filename = re.sub(r"\s+", " ", filename)
    return filename.strip()

def searchFile(query, file_records, limit=5, threshold=70):
    """
    Search file_records for files whose normalized names fuzzy-match the query.
    Returns a list of matched records with score above threshold.
    """

    # Prepare a list of preprocessed file names for matching
    processed_names = [preprocess_file_name(rec["file_name"]) for rec in file_records]

    # Preprocess query similarly
    query_proc = preprocess_file_name(query)

    # Use rapidfuzz to get best matches
    matches = process.extract(query_proc, processed_names, scorer=fuzz.partial_ratio, limit=4)
    for match, score, idx in matches:
        print(f"{match} → {score}")

    #matches = process.extract(query_proc, processed_names, scorer=fuzz.token_set_ratio, limit=limit)

    # Filter by threshold and map back to file_records
    results = []
    for match_name, score, idx in matches:
        if score >= threshold:
            matched_record = file_records[idx].copy()
            matched_record["score"] = score
            results.append(matched_record)

    return results
