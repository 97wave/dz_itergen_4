import hashlib

def hash_gen(input_path, output_path, index=0):
    with open (input_path, 'r', encoding='utf-8') as i:
        strings = i.readlines()
        
    while index < len(strings):
        string = strings[index]
        hash_object = hashlib.md5(string.encode())
        hash_string = (hash_object.hexdigest())
        
        with open (output_path, 'a', encoding='utf-8') as o:
            o.write(hash_string + '\n')

        yield index
        index += 1