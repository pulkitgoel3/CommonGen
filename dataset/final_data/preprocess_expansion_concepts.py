import json
import itertools

directory = "concept_relations"
dirpath = "commongen/commongen"
concept_filenames = ["train", "dev", "test"]

def create_concept_files(filename):
    read_file = directory + '/'+filename+".jsonl"
    data={}
    with open(read_file) as f:
        for line in f.readlines():
            concept_set = json.loads(line)["concept_set"]
            relations = json.loads(line)["expansion_concepts"]
            data[concept_set] = set(relations)

    key_text = []
    concept_list = []
    with open(dirpath + ".%s.cs_str.txt"%filename, 'r', encoding="utf8") as f1:
        for line in f1.readlines():
            key_text.append(line)

    with open(dirpath + ".%s.src_alpha.txt" % filename, 'r', encoding="utf8") as f1:
        for line in f1.readlines():
            concept_list.append(line)

    new_concept_list = []
    write_file = dirpath + '.'+filename+"_extended.txt"
    for i in range(len(key_text)):
        new_concepts = set(concept_list[i].split())
        added_concepts = data[key_text[i].strip()] - new_concepts
        new_concept_list.append(" ".join(new_concepts)+" "+" ".join(added_concepts))

    with open(write_file, "w") as f:
        f.write("\n".join(new_concept_list))


for filename in concept_filenames:
    create_concept_files(filename)


