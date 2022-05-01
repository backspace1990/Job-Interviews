def fin_top_20(canditdates):
    for candidat in candidates:
        course_scores = sum(candidat["scores"].values())
        scr_extr = candidat['extra_scores']
        candidat['scr_sum'] = course_scores + scr_extr

    candidates1 = sorted(candidates, key=lambda k : k['scr_sum'], reverse=True)
    winner_candidates=[]
    i = 0
    for W_candidates in candidates1:
        if i == 20:
            break
        winner_candidates.append(W_candidates['name'])
        i += 1
    return winner_candidates


def main():
    print(fin_top_20(canditdates=candidates))

if __name__ == '__main__':
    main()