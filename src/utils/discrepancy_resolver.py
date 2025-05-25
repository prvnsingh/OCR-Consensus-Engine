from collections import Counter
import Levenshtein
import logging
from itertools import combinations

def similarity(a, b):
    return Levenshtein.ratio(a, b)

def resolve_discrepancy(results: dict) -> str:
    engine_names = list(results.keys())
    outputs = list(results.values())

    logging.debug(f"OCR Outputs: {results}")

    # Case 1: All are the same
    if len(set(outputs)) == 1:
        logging.info("Exact match across all engines.")
        return outputs[0]

    # Case 2: Majority voting (2 out of 3 match exactly)
    counts = Counter(outputs)
    if counts.most_common(1)[0][1] >= 2:
        consensus = counts.most_common(1)[0][0]
        logging.info("Majority vote determined consensus.")
        return consensus

    # Case 3: Compute pairwise Levenshtein similarity
    scores = {name: 0 for name in engine_names}
    for (i, j) in combinations(range(len(outputs)), 2):
        s = similarity(outputs[i], outputs[j])
        scores[engine_names[i]] += s
        scores[engine_names[j]] += s

    for i in range(len(outputs)):
        logging.info(f"Levenshtein({engine_names[i]}) = {scores[engine_names[i]]:.3f}")

    best_engine = max(scores, key=scores.get)
    logging.info(f"Selected best text from: {best_engine} with score: {scores[best_engine]:.3f}")
    return results[best_engine]
