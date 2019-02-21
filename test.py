from synthesizer import synthesizer



wembs = ['/home/ur/data/Word_Vector/sgns.renmin.bigram.h5']

s = synthesizer((500, 500), (5, 10), (50, 60))

s.synthesize_image()




