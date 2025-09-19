import json, random
import nlpaug.augmenter.word as naw
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')


# load original data
with open("training_data_expanded.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(l) for l in f]

# synonym augmenter
aug = naw.SynonymAug(aug_src='wordnet')

expanded = []
for line in lines:
    # add original
    expanded.append(line)
    # create 3 light paraphrases of assistant and user messages
    for _ in range(3):
        new_line = json.loads(json.dumps(line))  # deep copy
        for m in new_line["messages"]:
            if m["role"] in ["user", "assistant"]:
                m["content"] = aug.augment(m["content"])
        expanded.append(new_line)

# save new file
with open("training_data_more_expanded.jsonl", "w", encoding="utf-8") as f:
    for l in expanded:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")

print(f"Expanded from {len(lines)} to {len(expanded)} lines.")
