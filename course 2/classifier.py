punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(s):
    for c in punctuation_chars:
        s = s.replace(c, "")
    return s    

def get_neg(s):
    s = s.lower()
    s = strip_punctuation(s)
    words = s.split()
    total = 0
    for w in words:
        if w in negative_words:
            total += 1
    return total

def get_pos(s):
    s = s.lower()
    s = strip_punctuation(s)
    words = s.split()
    total = 0
    for w in words:
        if w in positive_words:
            total += 1
    return total

with open("project_twitter_data.csv") as f:
    with open("resulting_data.csv", "w") as output:
        output.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
        for lin in f.readlines()[1:]:
            parts = lin.strip().split(",")
            s = parts[0]
            ret = parts[1]
            rep = parts[2]
            ps = get_pos(s)
            ns = get_neg(s)
            net = ps - ns
            output.write("{}, {}, {}, {}, {}".format(ret, rep, ps, ns, net))
            output.write("\n")
