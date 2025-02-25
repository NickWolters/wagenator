from transformers import AutoTokenizer, BertGenerationEncoder
import glob;
import os;

files = glob.glob('generated_samples/BERT/*')
for f in files:
    os.remove(f)

tokenizer = AutoTokenizer.from_pretrained("google/bert_for_seq_generation_L-24_bbc_encoder")
model = BertGenerationEncoder.from_pretrained("google/bert_for_seq_generation_L-24_bbc_encoder")

f = open("input_files/input_1.txt", "r")
prompt = f.read();

print("Given the following prompt : ", prompt)
for x in range (0, 10) :
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model(**inputs)

    print(tokenizer.decode(outputs))

    file_name = "generated_samples/BERT/bert-sample-{number}.{file_format}" 
    f = open(file_name.format(number = x, file_format = file_format), "w")
    f.write(''.join(tokenizer.decode(outputs)))
    f.write("\n ----------- \n\n".join(outputs))
    f.close() 
