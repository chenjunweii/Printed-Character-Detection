from tqdm import tqdm

def generate_character_dictionary_from_wembs(d, filename):

    with open(filename, 'r') as f:

        lines = f.readlines()

        for i, l in enumerate(tqdm(lines[1:])):

            l = l.split(' ')[:-1]

            if len(l[0]) == 1:
                
                d.append(l[0])

            elif len(l[0]) != 1:

                for t in l[0]:

                    if t not in d:

                        d.append(t)

        save_pickle(d, filename + '.pkl')



